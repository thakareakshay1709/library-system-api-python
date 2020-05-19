import flask
from flask_sqlalchemy import SQLAlchemy

# Database configuration and initialisation
db = SQLAlchemy()


class DatabaseContext:
    # Initialising database context
    def __init__(self, app: flask.app):
        app.app_context().push()
        db.init_app(app)
        db.create_all()
