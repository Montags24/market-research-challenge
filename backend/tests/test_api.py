import os
import pytest
import random
from dotenv import load_dotenv

from website import create_app
from website.utils import CHATBOT_MESSAGES

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, ".../.env"))

app = create_app()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_first_message_from_chatbot(client):
    route = "api/chatbot/response"
    payload = {}
    response = client.post(route, json=payload)
    assert response.status_code == 200
    assert response.json["message"] == "Success"
    assert response.json["chatbot_reply"]["body"] == CHATBOT_MESSAGES[0]["body"]


def test_reply_to_chatbot_with_available_responses(client):
    # Recieve the first message
    route = "api/chatbot/response"
    payload = {}
    response = client.post(route, json=payload)

    assert response.status_code == 200
    assert response.json["message"] == "Success"

    available_responses = response.json["chatbot_reply"]["responses"]
    payload["user_reply"] = random.choice(available_responses)
    payload["message_id"] = response.json["chatbot_reply"]["id"]

    response = client.post(route, json=payload)
    assert response.status_code == 200
    assert response.json["chatbot_reply"]["body"] == CHATBOT_MESSAGES[1]["body"]


def test_reply_to_chatbot_with_invalid_response(client):
    # Recieve the first message
    route = "api/chatbot/response"
    payload = {}
    response = client.post(route, json=payload)

    assert response.status_code == 200
    assert response.json["message"] == "Success"

    payload["user_reply"] = "invalid reponse"
    payload["message_id"] = response.json["chatbot_reply"]["id"]

    response = client.post(route, json=payload)
    assert response.status_code == 200
    assert response.json["rc"] == 16
    assert (
        response.json["message"] == "Error - Please choose from the available responses"
    )
