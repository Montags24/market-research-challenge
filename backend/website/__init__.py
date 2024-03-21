import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# create the holder for site config stuff
site_config = {}
site_config["instance_type"] = os.environ.get("instance_type")
site_config["this_url"] = os.environ.get("this_url")


def create_app():
    # This constructs the Flask application instance, and eliminates using it as a global variable, which can cause issues

    # Set the paths so that Flask knows where to look to serve up the static files
    this_directory = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_directory, "templates", "static")
    app = Flask(
        __name__,
        instance_relative_config=False,
        static_folder=static_folder,
        static_url_path="/static",
    )

    # app.config.from_object("config.Config")
    app.config.from_object(Config)

    with app.app_context():
        # now all the initiations
        db.init_app(app)
        migrate.init_app(app, db=db)

        from website import routes, models

        # To satisfy pylint
        routes, models = routes, models

        return app
