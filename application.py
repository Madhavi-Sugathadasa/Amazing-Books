from flask import Flask, render_template, session, request, jsonify
from flask_session import Session

app = Flask(__name__)

Session(app)

@app.route("/")
def index():
    return render_template("index.html")