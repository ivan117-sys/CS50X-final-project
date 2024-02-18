# YOUR PROJECT TITLE CS50 Review Website
#### Video Demo:  https://www.youtube.com/watch?v=zljNbHyIU48
#### Description: This is a website on wich you can review and browse all CS50 courses

Course Review Web App
Overview

This is a web application for reviewing courses. Users can log in, register, review courses, and view average ratings for each course. It utilizes Flask, SQLite, and CS50 library for backend functionalities and provides a simple web interface for users to interact with.

There is also an database wich uses sqlite and it utilizes 2 tables users and reviews

Features

User Authentication: Users can register, log in, and log out securely.
Course Reviews: Users can submit reviews for various courses.
Average Ratings: The application calculates and displays the average rating for each course.
Top Courses: The top three highest-rated courses are displayed on the homepage.

Technologies Used on backend:
Flask
SQLite
CS50 library
Werkzeug for password hashing

technologies used on the frontend:
HTML
CSS
Javascript
SASS
Bootsrap

Web site is created with design and responsive design in mind so it will look and feel good on all resolutions

Utility Functions and Decorators
Apology Function

The apology function is used to render an apology message to the user. It takes a message string and an optional HTTP status code as parameters and renders an apology HTML template with the provided message.

def apology(message, code=400):
    """Render message as an apology to user."""
    # Function code here
Login Required Decorator
The login_required decorator is used to decorate routes that require the user to be logged in. If the user is not logged in, they are redirected to the login page.

def login_required(f):
    """
    Decorate routes to require login.

This decorator ensures that certain routes can only be accessed by authenticated users, enhancing the security of the application.

Setup and Installation
Clone the repository to your local machine.
Ensure you have Python installed.
Install Flask and other dependencies by running:
Copy code
pip install -r requirements.txt
Run the application:
arduino
Copy code
flask run
Access the application in your web browser at http://localhost:5000.


File Structure
app.py: Contains the main Flask application code.
templates/: Contains HTML templates for rendering pages.
helpers.py: Contains helper functions for authentication and error handling.
static/: Contains static files such as CSS stylesheets and JavaScript scripts.
Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with any improvements or additional features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This project was created as part of the Harvard CS50x course.
