from flask_restful import Resource
from flask import request, jsonify
from context import db
from models import User
from services import Validator


class UserController(Resource):
    def __init__(self):
        self.validator = Validator()

    # Get method for endpoint /api/v1/resources/users/
    def get(self):
        # Fetching all users from database
        users = User.query.all()    # Querying Users table
        user_list = []
        for each_user in users:
            user_list.append(each_user.to_json())
        return jsonify(user_list)

    # Post method for endpoint /api/v1/resources/users/
    def post(self):
        # Fetching data from post request and adding it to variables
        username = request.json['username']
        email = request.json['email']

        # Validating empty username and email
        if not self.validator.user_validation(username,email):
            return dict(message="Incomplete details to add user or user already exists")

        else:
            # Adding user to Users table
            user = User(username=username,email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_json())
