from flask_restful import Resource
from flask import request, jsonify
from context import db
from models import User


class UserController(Resource):
    def get(self):
        # Fetching all users from database
        users = User.query.all()
        user_list = []
        for each_user in users:
            user_list.append(each_user.to_json())
        return jsonify(user_list)

    def post(self):
        # Fetching data from post request and adding it to variables
        username = request.json['username']
        email = request.json['email']
        # Need to add user validation here

        # Validating empty username and email
        if str(username).strip() == "" or str(email) == "":
            return dict(message="Incomplete details to add user")
        else:
            user = User(username=username,email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_json())
