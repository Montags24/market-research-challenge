from website import create_app, db
from website.models import User
import os
import pytest
from dotenv import load_dotenv

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, ".../.env"))

app = create_app()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test(client):

    pass
