import uuid

from flask_restful import Resource
from flask import request, jsonify
from context import db
from models import User, Book, Request
from services import RequestBusinessService, Validator


class RequestController(Resource):

    def __init__(self):
        self.requestBusinessService = RequestBusinessService()
        self.validatior = Validator()

    def post(self):
        # Fetching data from user request
        user_id = request.json['user_id']
        book_id = request.json['book_id']

        if (not str(user_id).strip().isdigit()) or str(book_id).strip() == "":
            return dict(message='Incorrect/Incomplete order details.')

        elif not self.validatior.request_validatior(user_id,book_id):
            return dict(message='Invalid user/book details.')

        else:
            books_issued,books_not_available = self.requestBusinessService.process_borrower_request(book_id)
            self.requestBusinessService.store_request_records(user_id, books_issued)
            db.session.commit()

            print("User ", user_id, " Books issued =", books_issued, " Total books issued = ", len(books_issued))
            return jsonify(dict(books_issued=books_issued, books_not_available=books_not_available))
