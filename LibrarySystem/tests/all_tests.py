import unittest
from context import DatabaseContext
from flask import Flask
from context import db
from flask_testing import TestCase
from models import User, Book


class MyFlaskTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///library-test.db"

    TESTING = True

    def create_app(self):
        """
        Method is used to create and return flask instance
        :return: Flask instance
        """
        app = Flask(__name__)
        DatabaseContext(app)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """
        Create all database instances with testing db
        :return: None
        """
        db.create_all()

    def tearDown(self):
        """
        Remove all database instances testing db
        :return:
        """
        db.session.remove()
        db.drop_all()


class AllTests(MyFlaskTest, unittest.TestCase):

    def test_user(self):

        user = User(username="admin", email="admin@admin.com")
        db.session.add(user)
        db.session.commit()

        # this works
        assert user in db.session

        response = self.client.get("/api/v1/resources/users/")
        # this raises an AssertionError
        assert user in db.session

    def test_books(self):
        book = Book(title="title", author="author", category="category", description="description",quantity=5)
        db.session.add(book)
        db.session.commit()

        # this works
        assert book in db.session

        self.client.get("/api/v1/resources/books/")
        # this raises an AssertionError
        assert book in db.session

if __name__ == '__main__':
    unittest.main()
