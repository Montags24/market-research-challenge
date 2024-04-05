import os
import pytest
from dotenv import load_dotenv

from website import create_app

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, ".../.env"))

app = create_app()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_question_bank_successful_response(client):
    api_package = {"questionBank": "welcome_question_bank"}

    response = client.post("/api/chatbot/question_bank", json=api_package)

    assert response.status_code == 200

    response_data = response.json
    assert response_data["rc"] == 0
    assert response_data["message"] == "Success"
    assert len(response_data["chatbot_questions"]) > 0


def test_get_question_bank_incorrect_key(client):
    api_package = {"questionBank": "invalid_key"}

    response = client.post("/api/chatbot/question_bank", json=api_package)

    assert response.status_code == 400

    response_data = response.json
    assert response_data["rc"] == 16
    assert response_data["message"] == "Error - survey does not exist in database"


def test_get_question_bank_invalid_payload(client):
    api_package = "{invalid}"

    response = client.post("/api/chatbot/question_bank", json=api_package)

    assert response.status_code == 500


def test_chatgpt_successful_response(client):
    api_package = {
        "user_reply": "Test reply",
        "previous_question": "Test question",
        "user_name": "test name",
    }

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
