from datetime import datetime

from context import db


class User(db.Model):
    """
    Model class of User, initialising db parameters.
    """
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(499), unique=True, index=True)
    email = db.Column(db.String(499), unique=True, index=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated = db.Column(db.DateTime, nullable=True)

    # Writing method to return json serializable object
    def to_json(self):
        return dict(id=self.id, username=self.username, email=self.email, created=self.created)

    def __repr__(self):
        return '<User %r>' % self.username
