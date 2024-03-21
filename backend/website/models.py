# from datetime import datetime, timedelta
# from flask import current_app as app
from website import db

from sqlalchemy.sql import func

# , expression, and_, or_


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    created_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return "<User {}>".format(self.name)
