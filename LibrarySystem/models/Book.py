from datetime import datetime
from context import db


class Book(db.Model):
    """
    Model class of Books table, initialising db parameters
    """
    __tablename__ = "Books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(499), unique=True, index=True)
    author = db.Column(db.String(99),nullable=False)
    category = db.Column(db.String(199),nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(499),nullable=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated = db.Column(db.DateTime, nullable=True)

    # Writing method to return json serializable object
    def to_json(self):
        return dict(id=self.id,title=self.title,author = self.author,category = self.category,
                    created=self.created,updated=self.updated,description = self.description)
    # Representation
    def __repr__(self):
        return '<Book %r>' % self.title
