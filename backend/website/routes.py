from flask import current_app as app
from flask import render_template, request, jsonify
from flask_cors import CORS
from website import db

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
@app.route("/index")
def index():
    # This is a vue project that serves the static index file only
    return render_template("index.html")


@app.route("/test")
def test_route():
    # This is a vue project that serves the static index file only
    return dict(message="Hello World")
