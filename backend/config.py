import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # The application entry point
    FLASK_APP = "wsgi.py"

    # Get .env variables
    SECRET_KEY = os.environ.get("SECRET_KEY")
    INSTANCE_TYPE = os.environ.get("INSTANCE_TYPE")
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_ADDRESS = os.environ.get("DB_ADDRESS")
    DB_PORT = os.environ.get("DB_PORT")
    DB_TYPE = os.environ.get("DB_TYPE")
    DB_NAME = os.environ.get("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"{DB_TYPE}://"
        + DB_USERNAME
        + ":"
        + DB_PASSWORD
        + "@"
        + DB_ADDRESS
        + ":"
        + DB_PORT
        + "/"
        + DB_NAME
    )


if __name__ == "__main__":
    config = Config()
