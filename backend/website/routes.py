from flask import current_app as app
from flask import render_template, request, jsonify
from flask_cors import CORS
from website import db
from website.chatgpt import generate_response
from website.utils import CHATBOT_MESSAGES


# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
@app.route("/index")
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")


@app.route("/api/chatbot/response", methods=["POST"])
def handle_user_response() -> dict:
    """
    This api will handle the responses from the user and return the next message from the chatbot.
    """
    try:
        api_package = request.get_json()

        try:
            user_reply = api_package["user_reply"]
            message_id = api_package["message_id"]
            previous_question = api_package["previous_question"]

            # check if user_response is part of the available responses
            if user_reply not in CHATBOT_MESSAGES[message_id]["responses"]:
                return dict(
                    rc=16, message="Error - Please choose from the available responses"
                )

            response = generate_response(
                user_reply=user_reply, previous_question=previous_question
            )

            chatgpt_reply = dict(
                id=None, sender="bot", body=response, timestamp=None, responses=[]
            )

            if message_id < len(CHATBOT_MESSAGES):
                return dict(
                    rc=0,
                    message="Success",
                    chatgpt_reply=chatgpt_reply,
                    chatbot_reply=CHATBOT_MESSAGES[message_id + 1],
                )
        except KeyError:
            # Handle the first message from chatbot where there is no user response
            return dict(rc=0, message="Success", chatbot_reply=CHATBOT_MESSAGES[0])

    except Exception as e:
        return dict(rc=16, message=f"An error occured - {e}")
