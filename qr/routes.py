from qr import app, mongo
from flask import request, render_template, redirect, url_for

atendee = mongo.db["atendee"]

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/atendees", methods = ["GET"])
def atendees():
    return render_template("atendees.html")

@app.route("/signin", methods = ["POST"])
def signin():
    user = request.form.to_dict()
    atendee.insert_one(user)
    return redirect(url_for("index"))