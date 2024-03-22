from flask import current_app as app
from flask import render_template, request
from flask_cors import CORS

# from website import db
from website.chatgpt import generate_chatgpt_response
from website.utils import CHATBOT_MESSAGES


# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


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
