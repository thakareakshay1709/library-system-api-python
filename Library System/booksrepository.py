# import SQLAlchemy as SQLAlchemy
from flask import Flask, jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
# Setting up debugger & environment variables for db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library-api.db'
app.config["DEBUG"] = True

# DB object
db = SQLAlchemy(app)


class User(db.Model):
    api_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def to_json(self):
        return dict(email=self.email, api_id=self.api_id)

    def __repr__(self):
        return '<User %r>' % self.username


class Books(db.Model):
    book_id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    book_title = db.Column(db.String(200),primary_key=False,unique=True,nullable=False)
    book_author = db.Column(db.String(150), primary_key=False, unique=False, nullable=False)
    book_category = db.Column(db.String(200), primary_key=False, nullable=False)
    book_available_quantity = db.Column(db.Integer)

    def to_json(self):
        return dict(book_id=self.book_id, book_title=self.book_title, book_author=self.book_author,book_category = self.book_category,book_available_quantity = self.book_available_quantity)

    def __repr__(self):
        return '<Book Title %r>' % self.book_title

db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


#POST methods to create users and insert dummy book records
@app.route("/api/v1/resources/users", methods=["POST"])
def create_user():
    user = User(email=request.json['email'],api_id =request.json['api_id'],password=request.json['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json());

@app.route("/api/v1/resources/newbooks", methods=["POST"])
def create_books():
    books = Books(book_id=request.json['book_id'],book_title=request.json['book_title'],book_author=request.json['book_author'],
                  book_category=request.json['book_category'],book_available_quantity=request.json['book_available_quantity'])
    db.session.add(books)
    db.session.commit()
    return jsonify(books.to_json())

@app.route("/api/v1/resources/books/borrow", methods=["POST"])
def request_books():
    books_not_available = []
    books_issued = []
    user_id = request.json['user_id']
    books_requested = request.json['books_requested']
    for book_id in books_requested:
        book = Books.query.get(book_id)
        if book is None:
            books_not_available.append(dict(book_name=book_id))
        else:
            if book.book_available_quantity == 0:
                books_not_available.append(dict(book_name=book.book_title))
            else:
                book.book_available_quantity = book.book_available_quantity - 1
                books_issued.append(dict(book_name=book.book_title))
    db.session.commit()
    print("User ",user_id," Books issued =",books_issued," Total books issued = ",len(books_issued))
    return jsonify(dict(books_issued=books_issued,books_not_available=books_not_available))

#Get Methods
# Filtering books by ID

# Fetching all books available in library
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    books = Books.query.all()
    books_list = []
    for b in books:
        books_list.append(b.to_json())
        print(b.book_id,b.book_title,b.book_author,b.book_category,b.book_available_quantity)
    return jsonify(books_list)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if ID is provided in request
    # If id is provided assign it to variable else raise error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: id field is not provided. Please provide book id'

    book_details = Books.query.filter_by(book_id = id).first()

    # Return books filtered from book id
    # Using jsonify function from flask convert list into JSON format
    return jsonify(book_details.to_json())


if __name__ == '__main__':
    app.run()
