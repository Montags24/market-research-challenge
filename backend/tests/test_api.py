import os
import pytest
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


def test_chatbot_successful_response(client):
    api_package = {"messageId": 0}

    response = client.post("/api/chatbot/response", json=api_package)

    assert response.status_code == 200

    response_data = response.json
    assert "rc" in response_data
    assert "message" in response_data
    assert "chatbot_reply" in response_data
    assert (
        response_data["chatbot_reply"]["body"]
        == CHATBOT_MESSAGES[api_package["messageId"] + 1]["body"]
    )


def test_chatbot_missing_message_id(client):
    api_package = {}

    response = client.post("/api/chatbot/response", json=api_package)

    assert response.status_code == 400

    response_data = response.json
    assert response_data["rc"] == 16
    assert response_data["message"] == "Error - wrong key provided"


def test_chatbot_invalid_message_id(client):
    api_package = {"messageId": 100}

    response = client.post("/api/chatbot/response", json=api_package)

    assert response.status_code == 400

    response_data = response.json
    assert response_data["rc"] == 16
    assert response_data["message"] == "Error - provided message ID is out of range"


def test_chatgpt_successful_response(client):
    api_package = {"user_reply": "Test reply", "previous_question": "Test question"}

    response = client.post("/api/chatgpt/response", json=api_package)

    assert response.status_code == 200

    response_data = response.json
    assert "rc" in response_data
    assert "message" in response_data
    assert "chatgpt_reply" in response_data


def test_chatgpt_missing_keys(client):
    api_package = {"some_other_key": "Test value"}

    response = client.post("/api/chatgpt/response", json=api_package)

    assert response.status_code == 400

    response_data = response.json
    assert response_data["rc"] == 16
    assert response_data["message"] == "Error - required key(s) not found"


def test_chatgpt_unexpected_error(client):
    # Simulate an unexpected error by providing an invalid JSON payload
    invalid_json = "{invalid}"

    # Make a POST request with the invalid JSON payload
    response = client.post(
        "/api/chatgpt/response", data=invalid_json, content_type="application/json"
    )

    assert response.status_code == 500

    response_data = response.json
    assert response_data["rc"] == 16
    assert "An error occurred" in response_data["message"]
