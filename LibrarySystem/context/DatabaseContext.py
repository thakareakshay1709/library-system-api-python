import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DatabaseContext:

    def __init__(self, app: flask.app):
        db.init_app(app)
