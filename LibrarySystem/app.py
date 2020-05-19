from flask import Flask
from flask_restful import Api

from controllers import BookController, UserController, RequestController

from context import DatabaseContext

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

config = app.config

api = Api(app)

database_context = DatabaseContext(app)

api.add_resource(BookController, '/api/v1/resources/books/')

api.add_resource(UserController, '/api/v1/resources/users/')

api.add_resource(RequestController, '/api/v1/resources/books/requests/')


@app.route("/")
def index():
    return "Library System"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
