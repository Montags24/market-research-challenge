import requests
import os
from dotenv import load_dotenv

from flask import current_app as app
from flask import render_template, request, jsonify
from flask_cors import CORS

# from website import db
from website.chatgpt import generate_chatgpt_response
from website.surveys import QUESTION_BANK

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, "../.env"))


@app.route("/")
@app.route("/index")
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")


@app.route("/api/chatbot/question_bank", methods=["POST"])
def get_chatbot_questions() -> dict:
    """Endpoint to retrieve chatbot questions based on the provided question bank.

    Returns:
        dict: A dictionary containing the chatbot questions along with a return code and message.
    """
    try:
        api_package = request.get_json()

        question_bank = api_package["questionBank"]
        chatbot_questions = QUESTION_BANK[question_bank]

        return dict(rc=0, chatbot_questions=chatbot_questions, message="Success"), 200

    except KeyError:
        return (
            jsonify(
                rc=16,
                message="Error - survey does not exist in database",
            ),
            400,
        )
    except Exception as e:
        return jsonify(rc=16, message=f"An error occurred - {e}"), 500


@app.route("/api/chatgpt/response", methods=["POST"])
def handle_user_response() -> dict:
    """
    Handles user responses and generates a response from ChatGPT.

    Returns:
        dict: A dictionary containing the response status and the ChatGPT reply.
            If successful, returns the ChatGPT reply along with a success message.
            If an error occurs, returns an error code and message.

    Raises:
        KeyError: If required keys "user_reply" or "previous_question" are not provided in the request JSON.
        Exception: If an unexpected error occurs.

    """
    try:
        api_package = request.get_json()

        try:
            user_reply = api_package["user_reply"]
            previous_question = api_package["previous_question"]
            user_name = api_package["user_name"]

            # Generate response from ChatGPT
            response = generate_chatgpt_response(
                user_reply=user_reply,
                previous_question=previous_question,
                user_name=user_name,
            )

            chatgpt_reply = dict(
                id=None, sender="bot", body=response, timestamp=None, responses=[]
            )

            return (
                jsonify(
                    rc=0,
                    message="Success",
                    chatgpt_reply=chatgpt_reply,
                ),
                200,
            )
        except KeyError:
            return jsonify(rc=16, message="Error - required key(s) not found"), 400

    except Exception as e:
        return jsonify(rc=16, message=f"An error occurred - {e}"), 500


@app.route("/auth/google/callback", methods=["POST"])
def google_callback():
    try:
        # Get the authorization code from the request
        api_package = request.get_json()
        code = api_package.get("code")
        if not code:
            raise ValueError("Authorization code not provided")

        # Exchange the authorization code for an access token
        token_response = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": os.environ.get("GOOGLE_OAUTH_CLIENT_ID"),
                "client_secret": os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET"),
                "redirect_uri": os.environ.get("GOOGLE_OAUTH_REDIRECT_URL"),
                "grant_type": "authorization_code",
            },
        )
        return_message = {
            "code": code,
            "client_id": os.environ.get("GOOGLE_OAUTH_CLIENT_ID"),
            "client_secret": os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET"),
            "redirect_uri": os.environ.get("GOOGLE_OAUTH_REDIRECT_URL"),
            "grant_type": "authorization_code",
        }
        token_response.raise_for_status()  # Raise exception for non-2xx status codes
        token_data = token_response.json()
        access_token = token_data.get("access_token")
        if not access_token:
            return (
                jsonify(rc=16, message="Access token not found in token response"),
                400,
            )

        # Fetch user data using the access token
        user_response = requests.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        user_response.raise_for_status()  # Raise exception for non-2xx status codes
        user_data = user_response.json()

        return jsonify(rc=0, user_data=user_data, message="Success"), 200

    except requests.RequestException as e:
        return (
            jsonify(
                rc=16, message=f"Google API request failed: {str(e)} - {return_message}"
            ),
            500,
        )

    except ValueError as ve:
        return jsonify(rc=16, message=str(ve)), 400
    except Exception as ex:
        return jsonify(rc=16, message=f"An error occurred: {str(ex)}"), 500
