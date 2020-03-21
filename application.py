import os, hashlib, requests

from flask import Flask, render_template, session, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from math import floor

app = Flask(__name__)

# Check for environment variables
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
if not os.getenv("GOODREADS_API_KEY"):
    raise RuntimeError("GOODREADS_API_KEY is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    #clear session variables
    session["user_id"] = None
    session["username"] = None
    session["book_id"] = None
    session["work_rating_count"] = None
    session["average_rating"] = None
    session["average_rating_int"] = None
    
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    """Register a new user"""
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirmpassword")
    
    #check required fields entered
    if username is None or (len(username.strip()) == 0):
         return render_template("index.html", message_register="Please enter username field.", message_danger=1 )
    if password is None or (len(password.strip()) == 0):
         return render_template("index.html", message_register="Please enter password field.", message_danger=1)
    if password is None or (len(password.strip()) == 0):
         return render_template("index.html", message_register="Please enter confirm password field.", message_danger=1)
    
    #check password and confirm password fiels are match
    if password != confirm_password:
        return render_template("index.html", message_register="Those passwords didn't match. Try Again", message_danger=1, )
    
    #make username not case sensitive
    username = username.lower()
    
    # check wheather user already exists.
    if db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount != 0:
        return render_template("index.html", message_register="That username is taken. Try another.", message_danger=1)
    
    #make passwors hash with md5
    password_hash = hashlib.md5(password.encode())
    db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": username, "password": password_hash.hexdigest()})
    db.commit()
    return render_template("index.html", message_register="You have successfully registered.", message_danger=0)


@app.route("/login", methods=["POST"])
def login():
    """User Login"""
    
    username = request.form.get("username")
    password = request.form.get("password")
    
    #check required fields entered
    if username is None or (len(username.strip()) == 0):
         return render_template("index.html", message_login="Please enter username field.")
    if password is None or (len(password.strip()) == 0):
         return render_template("index.html", message_login="Please enter password field.")
    
    #create passowrd hash
    password_hash = hashlib.md5(password.encode())
    
    #make username not case sensitive
    username = username.lower()
    
    user = db.execute("SELECT * FROM users WHERE username = :username AND password = :password", {"username": username, "password": password_hash.hexdigest() }).fetchone()
    
    if user is None:
         return render_template("index.html", message_login = "Invalid username or password")
    
    #set session variables
    session["user_id"] = user.id
    session["username"] = user.username
    
    return render_template("welcome.html", username = session["username"])

@app.route("/logout")
def logout():
    """User logout"""
    
    #clear session variables
    session["user_id"] = None
    session["username"] = None
    session["book_id"] = None
    session["work_rating_count"] = None
    session["average_rating"] = None
    session["average_rating_int"] = None
    
    return render_template("index.html")
