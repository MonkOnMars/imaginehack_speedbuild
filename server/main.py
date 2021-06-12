from flask import Flask, jsonify, abort, request, render_template, redirect, url_for
from flaskext.mysql import MySQL

import secrets
import hashlib

salt = b"brofist"  # the current salt for all password hashing

app = Flask(__name__)

mysql = MySQL(
    app,
    prefix="test",
    host="localhost",
    user="abc",
    password="abc",
    db="game",
    autocommit=True, # auto commit and every database function
)
mysql.init_app(app)


"""
Main page for displaying information of this website,
who are we, what we do, what you can do...
"""


@app.route("/")
def index():
    return render_template("index.html")


"""
A register page to enable the feature for tracking user progress?
"""


@app.route("/register", methods=["GET", "POST"])
def register():
    cursor = mysql.get_db().cursor()
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        password = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=salt,
            iterations=100
        )
        password = password.hex()

        cursor.execute("insert into user (username,password) values (%s,%s)", (username, password))

        return redirect(url_for("index"))
    else:
        return """
        <form action="/register" method="POST">  
            <label>Username : </label>   
            <input type="text" placeholder="Enter Username" name="username" required>  
            <label>Password : </label>   
            <input type="password" placeholder="Enter Password" name="password" required>  
            <button type="submit">Register</button>   
            <input type="checkbox" checked="checked"> Remember me   
            <button type="button" class="cancelbtn"> Cancel</button>   
            Forgot <a href="#"> password? </a>   
        </form>  
        """


"""
The login page
"""
@app.route("/login", methods=["GET", "POST"])
def login():
    cursor = mysql.get_db().cursor()

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        password = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=salt,
            iterations=100
        )
        password = password.hex()

        selectedCount = cursor.execute("select username,password from user where username=%s and password=%s", (username, password))
        if selectedCount < 1:
            return "wrong username/password"
        else:
            s = f"Welcome! {username} {password}"
            return s
    else:
        return """
        <form action="/login" method="POST">  
            <label>Username : </label>   
            <input type="text" placeholder="Enter Username" name="username" required>  
            <label>Password : </label>   
            <input type="password" placeholder="Enter Password" name="password" required>  
            <button type="submit">Login</button>   
            <input type="checkbox" checked="checked"> Remember me   
            <button type="button" class="cancelbtn"> Cancel</button>   
            Forgot <a href="#"> password? </a>   
        </form>  
        """


"""
The page where the game is staying in
"""
@app.route("/game")
def game():
    return "Game page"


"""
The page where you exchange your coins for a donation on a course
"""


@app.route("/market", methods=["GET", "POST"])
def market():
    cursor = mysql.get_db().cursor()
    if request.method == "GET":
        cursor.execute("select * from market_data")
        allCourse = cursor.fetchall()

        courseListing = []
        for course in allCourse:
            tmp = {}
            tmp["course_name"] = course[1]
            tmp["currency"] = course[2]
            tmp["current_available_funds"] = course[3]
            tmp["funding_people_count"] = course[4]
            # tmp["course_name"] = course[1]
            # tmp["start_date"] = course[2]
            # tmp["end_date"] = course[3]
            # tmp["currency"] = course[4]
            # tmp["cost"] = course[5]
            # tmp["current_available_funds"] = course[6]
            # tmp["funding_people_count"] = course[7]
            courseListing.append(tmp)

        return render_template("market.html", courseListing=courseListing)


"""
backend api for interacting with game updates, game info, player status
"""
@app.route("/api", methods=["POST"])
def api():
    userJSON = request.get_json()

    return jsonify(
        gameData={
            "lvl": 3,
            "lvlSeed": secrets.token_hex(nbytes=16),  # the obstacle can be generated using these seed
        }
    )


"""
Custom status_code rendering?
"""
@app.errorhandler(404)
def page_not_found(error):
    return "404 this page is not found"


@app.errorhandler(405)
def method_not_allowed(error):
    return error


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=33433,
        debug=True
    )
