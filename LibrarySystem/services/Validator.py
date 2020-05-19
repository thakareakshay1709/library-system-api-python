from context import db
from models import Book, Request, User


class Validator:

    def book_validation(self, title, author, category, quantity) -> bool:
        """
        Validating books detail
        :param title: Book title
        :param author: Book author
        :param category: Book category
        :param quantity: Book quantity
        :return: True if details correct, complete and unique otherwise False
        """
        if str(title).strip() == "" or str(author).strip() == "" or str(category).strip() == "" or int(
                quantity) < 1 or quantity is None:
            return False
        elif not Book.query.filter_by(title=title).first():
            return True

    def user_validation(self, username, email) -> bool:
        """
        Validating username and email.
        :param username: User username
        :param email: User email
        :return: True if credentials exist in User table otherwise False
        """
        print("Services user_validation -> ", username, email)
        if not (str(username).strip() == "" or str(email).strip() == ""):
            fetched_email = User.query.filter_by(email=email).first()
            fetched_username = User.query.filter_by(username=username).first()

            print("Fetched ",fetched_email,fetched_username)
            if  fetched_email is None or fetched_username is None:
                return True
            else:
                return False


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
            if db_user is None:
                return False
            elif int(user_id) == db_user.id:
                return True

        return False
