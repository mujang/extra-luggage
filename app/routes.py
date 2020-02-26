from flask import render_template
from app import app


@app.route("/")
def home():
    return render_template("home.html",title="Home")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html",title="About Us",)

@app.route("/frequentlyaskquestions")
def frequentlyaskquestions():
    return render_template("frequentlyaskquestions.html",title="Frequently Ask Question")

@app.route("/routes")
def routes():
    return "routes"

@app.route("/login")
def login():
    return "login"