import requests
import os
from dotenv import load_dotenv

from flask import current_app as app
from flask import render_template, request, jsonify
from flask_cors import CORS

# from website import db
from website.chatgpt import generate_chatgpt_response
from website.utils import CHATBOT_MESSAGES

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, "../.env"))


@app.route("/")
@app.route("/index")
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")


@app.route("/api/chatbot/response", methods=["POST"])
def get_next_message_from_chatbot() -> dict:
    """
    Get the next message from the chatbot based on the provided message ID.

    Returns:
        dict: A dictionary containing the response status and the next chatbot message.
            If successful, returns the next chatbot message along with a success message.
            If an error occurs, returns an error code and message.

    Raises:
        KeyError: If the required key "messageId" is not provided in the request JSON.
        IndexError: If the provided message ID is out of range of available chatbot messages.
        Exception: If an unexpected error occurs.

    """
    try:
        api_package = request.get_json()

        try:
            message_id = api_package["messageId"]

            if message_id < len(CHATBOT_MESSAGES):
                return (
                    jsonify(
                        rc=0,
                        message="Success",
                        chatbot_reply=CHATBOT_MESSAGES[message_id + 1],
                    ),
                    200,
                )
            else:
                raise IndexError("Provided message ID is out of range.")

        except KeyError:
            return (
                jsonify(
                    rc=16,
                    message="Error - wrong key provided",
                ),
                400,
            )

    except IndexError:
        return (
            jsonify(
                rc=16,
                message="Error - provided message ID is out of range",
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
        return jsonify(rc=16, message=f"Google API request failed: {str(e)}"), 500

    except ValueError as ve:
        return jsonify(rc=16, message=str(ve)), 400
    except Exception as ex:
        return jsonify(rc=16, message=f"An error occurred: {str(ex)}"), 500
