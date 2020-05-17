import json

from flask import request, jsonify
from flask_restful import Resource
from context import db
from models import Book


class BookController(Resource):

    def get(self):
        books = Book.query.all()
        books_list = []
        for each_book in books:
            books_list.append(each_book.to_json())
        return jsonify(books_list)

    def post(self):
        # Fetching parameters from request
        title = request.json['title']
        author = request.json['author']
        category = request.json['category']
        description = request.json['description']
        quantity = request.json['quantity']

        if str(title).strip() == "" or str(author).strip() == "" or str(category).strip() == "" or int(
                quantity) < 1:
            return dict(message="Incomplete parameters to add book")
        else:
            book = Book(title=title, author=author, category=category, description=description, quantity=quantity)
            db.session.add(book)
            db.session.commit()
            return jsonify(book.to_json())
