import os

from config import config
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

env = os.getenv("FLASK_ENV", "development")
app.config.from_object(config[env])

db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("login_succes.html")

    return render_template("login.html")


app.run(host="0.0.0.0", port=81)
