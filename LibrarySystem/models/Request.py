from datetime import datetime, timedelta
from context import db


class Request(db.Model):
    """
    Model class of request initialising db parameters.
    """
    __tablename__ = "Request"

    id = db.Column(db.String(20), primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    due_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.now() + timedelta(days=30))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated = db.Column(db.DateTime, nullable=True)
    r_book_title = db.Column(db.String(499), nullable=False)
    qty_available = db.Column(db.Integer, nullable=False)

    # Writing method to return json serializable object
    def to_json(self):
        return dict(id=self.id, user_id=self.user_id, book_id=self.book_id, r_book_title=self.r_book_title,
                    issue_date=self.issue_date,
                    due_date=self.due_date, qty_ordered=self.qty_ordered, qty_available=self.qty_available)

    def __repr__(self):
        return '<Request %r>' % self.id
