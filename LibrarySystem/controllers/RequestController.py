import uuid

from flask_restful import Resource
from flask import request, jsonify
from context import db
from models import Request
from services import RequestBusinessService, Validator


class RequestController(Resource):

    def __init__(self):
        self.requestBusinessService = RequestBusinessService()
        self.validatior = Validator()

    # Get method for endpoint /api/v1/resources/books/requests/
    def get(self):
        requests = Request.query.all()  # Querying Books table
        book_request = []
        for req in requests:
            book_request.append(req.to_json())
        if len(book_request) == 0:
            print("Available books in db = ", len(book_request))
            return dict(message="No requests in table")
        else:
            return jsonify(book_request)

    # Post method for endpoint /api/v1/resources/books/requests/
    def post(self):
        # Fetching data from user request
        user_id = request.json['user_id']
        book_id = request.json['book_id']

        # Removing duplicate book requests
        book_set = set()
        for unique in book_id:
            book_set.add(unique)

        # Input validation
        if (not str(user_id).strip().isdigit()) or str(book_set).strip() == "":
            return dict(message='Incorrect/Incomplete order details.')

        elif not self.validatior.request_validatior(user_id,book_set):
            return dict(message='Invalid user/book details.')

        # Calling services to process requests
        else:
            books_issued,books_not_available = self.requestBusinessService.process_borrower_request(book_set)
            self.requestBusinessService.store_request_records(user_id, books_issued)
            db.session.commit()

            print("User ", user_id, " Books issued =", books_issued, " Total books issued = ", len(books_issued))
            return jsonify(dict(books_issued=books_issued, books_not_available=books_not_available))
