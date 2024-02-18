from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import os

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 library to use SQlite database
db = SQL("sqlite:///cs50.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():

  if request.method == "POST":

    # Get user data 
    data = request.get_json()

    user_title = data["title"]
    user_review = int(data["review"])

    # Get data from database

    rows = db.execute(
      "SELECT * FROM reviews WHERE title = ? AND user_id = ?", user_title, session["user_id"]
    )

    if len(rows) != 1:

      db.execute(
        "INSERT INTO reviews (title, review, user_id) VALUES(?, ?, ?)", user_title,user_review, session["user_id"] 
      )
    
    else:
      db.execute(
        "UPDATE reviews SET review = ? WHERE title = ? AND user_id = ?", user_review, user_title, session["user_id"] 
      )
      
  else:
   
   avg_review_x = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50X'"
      )
   
   avg_review_p = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50P'"
      )
   
   avg_review_c = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50CYBER'"
      )
   
   avg_review_a = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50AI'"
      )
   
   avg_review_w = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50W'"
      )
   
   avg_review_sq = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50SQL'"
      )
   
   avg_review_m = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50M'"
      )
   
   avg_review_t = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50T'"
      )
   
   avg_review_g = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50G'"
      )
   
   avg_review_r = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50R'"
      )
   
   avg_review_ap = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50AP'"
      )
   
   avg_review_b = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50B'"
      )
   
   avg_review_os = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS5OS'"
      )
   
   avg_review_l = db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = 'CS50L'"
      )
   
   best = db.execute(
     "SELECT title, AVG(review) FROM reviews GROUP BY title ORDER BY review DESC LIMIT 3" 
   )

   print(best)
   
   return render_template("index.html", 
                          review_x = avg_review_x[0]['AVG(review)'], 
                          review_p = avg_review_p[0]['AVG(review)'], 
                          review_c = avg_review_c[0]['AVG(review)'], 
                          review_a = avg_review_a[0]['AVG(review)'],
                          review_w = avg_review_w[0]['AVG(review)'],
                          review_sq = avg_review_sq[0]['AVG(review)'],
                          review_m = avg_review_m[0]['AVG(review)'],
                          review_t = avg_review_t[0]['AVG(review)'],
                          review_g = avg_review_g[0]['AVG(review)'],
                          review_r = avg_review_r[0]['AVG(review)'],
                          review_ap = avg_review_ap[0]['AVG(review)'],
                          review_b = avg_review_b[0]['AVG(review)'],
                          review_os = avg_review_os[0]['AVG(review)'],
                          review_l = avg_review_l[0]['AVG(review)'],
                          best_courses = best)
  
  return jsonify(db.execute(
        "SELECT AVG(review) FROM reviews WHERE title = ?", user_title
      ))

@app.route("/login", methods=["GET", "POST"])
def login():

  # Log user in

  # Forget any user_id
  session.clear()

  if request.method == "POST":
   username = request.form.get("username")
   password = request.form.get("password")

  #  Ensure username was submitted
   if not username:
     return apology("must provide username", 403)
   elif not password:
     return apology("must provide password", 403)
   
  #  Query database for username
   rows = db.execute(
     "SELECT * FROM users WHERE username = ?", username
   )

  #  Ensure username and passwrod are correct
   
   if len(rows) != 1 or not check_password_hash(
     rows[0]["hash"], password
   ):
     return apology("Invalid username and/or password", 403)
   
  #  Remember wich user has logged in
   
   session["user_id"] = rows[0]["user_id"]
   session["username"] = username
   

  #  Redirect user to homepage
   flash("Welcome!", "success")
   return redirect("/")

  else:
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
  # "Register user"

  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirmation")

    # Check if username is already in the database
    rows = db.execute(
      "SELECT * FROM users WHERE username = ?", username
    )

    print(username, password, confirm_password)

    # Ceck for error
    if not username:
      return apology("must provide username", 400)
    
    elif not password:
      return apology("must provide password", 400)
    
    elif password != confirm_password:
      return apology("Passwords dont match", 400)
    
    # Hash paswword
    hashedPassword = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)

    # Add user to database
    db.execute(
      "INSERT INTO users (username, hash) VALUES(?, ?)", username,hashedPassword 
    )

    # Start session
    session["user_id"] = username
    session["username"] = username

    # Redirect user to homepage
    flash("Welcome!", "success")
    return redirect("/")

  else:
    return render_template("register.html")
  
@app.route("/logout")
def logout():
  # Log user out

  # Forget any user_id
  session.clear()

  # Redirect user to login form
  return redirect("/")