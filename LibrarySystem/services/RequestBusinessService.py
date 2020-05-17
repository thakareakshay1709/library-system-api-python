import uuid
from context import db
from models import Book, Request


class RequestBusinessService:

    def process_borrower_request(self,book_id) -> tuple:
        """
        Process the user request to issue books and store it in issued and not
        available list according to the quantity of books in inventory
        :param book_id: Array of book ids
        :return: tuple (issued books, not available books)
        """

        # Create empty list
        books_not_available = []
        books_issued = []

        for b_id in book_id:
            book = Book.query.get(b_id) # Querying books table
            if book is None:
                # If books are not in table, apend list
                books_not_available.append(dict(b_id=b_id))
            else:
                # If books quantity = 0, apend not available list
                if book.quantity == 0:
                    books_not_available.append(dict(book_id=book.id, book_name=book.title))
                else:
                    # If books are available and issued, reduce the book quantity
                    book.quantity = book.quantity - 1
                    books_issued.append(dict(book_id=book.id, book_name=book.title))
        return books_issued, books_not_available

    def store_request_records(self, user_id, books_issued ) -> None:
        """
        Storing user request to borrow books into database. Table -> Request
        :param user_id: registered borrower
        :param books_issued: Array of books id requested
        :return: None
        """
        # Generating unique id
        id = str(uuid.uuid4())

        # Looping through the array of books issued and store individual record
        for book in books_issued:
            bk = Book.query.get(book.get('book_id'))    # Querying Books table
            qty = bk.quantity
            print(bk, qty)
            req = Request(id=id, user_id=user_id, book_id=book.get('book_id'),
                          r_book_title=book.get('book_name'), qty_available=qty)
            db.session.add(req)

