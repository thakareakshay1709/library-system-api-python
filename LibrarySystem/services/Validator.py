from context import db
from models import Book, Request, User


class Validator:
    def user_validation(self, username, email) -> bool:
        """
        Validating username and email.
        :param username: User username
        :param email: User email
        :return: True if credentials exist in User table otherwise False
        """
        print("Services user_validation -> ", username, email)
        return True

    def request_validatior(self, user_id, book_id) -> bool:
        """
        Validating registered user details and book id details
        :param user_id: id from Users table
        :param book_id: id from Books table
        :return: True if details exist in tables otherwise false
        """
        print("Services request_validatior -> ", user_id, book_id)
        if str(user_id).strip() != "" and len(list(book_id)) != 0:
            db_user: User = User.query.get(user_id)
            print(db_user)
            if int(user_id) == db_user.id:
                return True

        return False
