import requests
import os
from dotenv import load_dotenv

from flask import current_app as app
from flask import render_template, request
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
                    dict(
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
                dict(
                    rc=16,
                    message="Error - wrong key provided",
                ),
                400,
            )

    except IndexError:
        return (
            dict(
                rc=16,
                message="Error - provided message ID is out of range",
            ),
            400,
        )

    except Exception as e:
        return dict(rc=16, message=f"An error occurred - {e}"), 500


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
                dict(
                    rc=0,
                    message="Success",
                    chatgpt_reply=chatgpt_reply,
                ),
                200,
            )
        except KeyError:
            return dict(rc=16, message="Error - required key(s) not found"), 400

    except Exception as e:
        return dict(rc=16, message=f"An error occurred - {e}"), 500


@app.route("/auth/google/callback", methods=["POST"])
def google_callback():
    # Get the authorization code from the request
    api_package = request.get_json()
    code = api_package["code"]

    # Exchange the authorization code for an access token
    # You should replace the placeholders with your actual client ID, client secret, and redirect URI
    uri = os.environ.get("GOOGLE_OAUTH_REDIRECT_URL")
    response = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "code": code,
            "client_id": os.environ.get("GOOGLE_OAUTH_CLIENT_ID"),
            "client_secret": os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET"),
            "redirect_uri": os.environ.get("GOOGLE_OAUTH_REDIRECT_URL"),
            "grant_type": "authorization_code",
        },
    )

    # If the response is successful, parse the access token from the response
    if response.status_code == 200:
        data = response.json()
        access_token = data.get("access_token")

        # If we have an access token, fetch the user's details
        if access_token:
            response = requests.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )

            # If the response is successful, parse the user's details from the response
            if response.status_code == 200:
                user_data = response.json()
                # Do something with the user's data, e.g. save it to your database
                return {"status": "success", "data": user_data}
            else:
                return {"status": "error", "message": "Failed to fetch user data"}
        else:
            return {"status": "error", "message": "Failed to get access token"}
    else:
        return {"status": "error", "message": "Failed to exchange authorization code"}
