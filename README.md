
Task -

Please use python 3 and above

Design a library system where the user submits request to borrow one or more books.
- Write an API that has a post method.
- It should receive the incoming request and store it in a database.
 
Code is evaluated on the basis of 
- Programming practices.
- Design choice.
- Functionality
- Accuracy

Bonus points:
- For using an ORM
- For a Dockerfile.

DO provide a readme file to get a better understanding
*************************************************************

---->Readme<----

****Technical stack****
1. Python 3.8
2. Flask - Python web framework
3. SQLAlchemy - For ORM purpose
4. Sqlite3 - Database
5. Postman - For post and get methods
6. Docker Toolbox (Could not install Docker desktop because of system prerequisite)

****Project package includes****

Python Project - LibrarySystem
Dockerfile
requirements.txt
library-new.db
Readme
Output images - proof of running project of both local machine and docker 

****Project Description****

****Functionality description
Library api system is implemented where only register users are able to query the database
in order to see the available books and borrow the books.

Once user is registered, he is able to borrow one or multiple books from available books. All the information
regarding users, books and requests is saved in relevant tables.

All types of user validations and few test cases are written in order to prevent incorrect data.

****Assumptions
1. Request to borrow books will be in array containing book ids
2. All input parameters will be in json format and in provided in same format as mentioned in examples
3. Docker environment will already be set up with docker image
4. Two test cases are provided to show basic test cases

****Endpoints

Endpoints are routed to same path for both GET and POST. It will show results in json format according to method type.
GET method returns the json output
POST method requires json input (Mandatory)


http://127.0.0.1/5000/api/v1/resources/books/
http://127.0.0.1/5000/api/v1/resources/users/
http://127.0.0.1/5000/api/v1/resources/books/requests/

****Run code on local machine
1. Download and extract the project folder 'Akshay_Thakare_Library_Project'
2. Copy LibrarySystem into local workspace directory
3. Configure the virtual environment on PyCharm (Used this IDE)
4. Run app.py python file
5. Provide POST parameters to above endpoints
6. Sample example to test the output is given below and in 'Output Postman local and docker images' folder

****Run code on docker
1. I assume image can be built with respect to provided dockerfile and requirements.txt file
2. Check docker image with command (docker images)
3. Check running container with command (docker container ls -all)
4. Build docker image with command (docker build . -t library-system) (library-system is name of image)
5. Now check if container status is exitted. Run command (docker run -d -p 5000:5000 library-system)
6. Check docker logs with command (docker logs containerID)


****Examples/Format to run and test application
1. Get requests can be called directly as per given end points above
2. For POST requests follow structure below,

To create users
{
	"email" : "akshay@ucd.com",
	"username": "Akshay"
}

To create books
{
	"title" : "Measures What Measures",
	"author": "Jeff",
	"category": "Personality Development",
	"quantity": 10,
	"description":"Growth 10X"
}

To create requests

{
	"user_id" : 2,
	"book_id" : [1,2,3]
}

Output -

Please find the output folder for reference

******Reference sites used while development*******

https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
https://pypi.org/project/flask-expects-json/
https://pythonhosted.org/Flask-Inputs/
https://www.flaskapi.org/api-guide/status-codes/
https://flask.palletsprojects.com/en/1.1.x/testing/
https://flask-restful.readthedocs.io/en/latest/quickstart.html#endpoints
http://exploreflask.com/en/latest/storing.html#sqlalchemy
https://www.wintellect.com/containerize-python-app-5-minutes/
https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt
https://flask.palletsprojects.com/en/1.1.x/#user-s-guide

