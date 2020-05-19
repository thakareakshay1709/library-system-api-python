
from flask import request, jsonify
from flask_restful import Resource
from context import db
from models import Book
from services import Validator


class BookController(Resource):

    def __init__(self):
        self.validator = Validator()

    # Get method for endpoint /api/v1/resources/books/
    def get(self):
        books = Book.query.all()    # Querying Books table
        books_list = []
        for each_book in books:
            books_list.append(each_book.to_json())
        if len(books_list) == 0:
            print("Number of books in table = ", len(books_list))
            return dict(message="No books available")

        return jsonify(books_list)

    # Post method for endpoint /api/v1/resources/books/
    def post(self):
        # Fetching parameters from request
        title = request.json['title']
        author = request.json['author']
        category = request.json['category']
        description = request.json['description']
        quantity = request.json['quantity']

        # Validation of user inputs
        if not self.validator.book_validation(title, author, category, quantity):
            return dict(message="Incomplete/Invalid details to add book or book title already exists")
        else:
            # Adding book to Books table
            book = Book(title=title, author=author, category=category, description=description, quantity=quantity)
            db.session.add(book)
            db.session.commit()
            return jsonify(book.to_json())
