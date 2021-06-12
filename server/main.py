from flask import Flask, jsonify, abort, request, render_template, redirect, url_for 
from flaskext.mysql import MySQL

import secrets
import hashlib

app = Flask(__name__)

mysql = MySQL(
    app,
    prefix="test",
    host="localhost",
    user="abc",
    password="abc",
    db="game",
    autocommit=True,
)
mysql.init_app(app)



"""
Main page for displaying information of this website,
who are we, what we do, what you can do...
"""
@app.route("/")
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute("select * from user")
    d = cursor.fetchall()

    out = []
    for row in d:
        out.append(str(row))

    return render_template("index.jinja",out=out)


"""
A register page to enable the feature for tracking user progress?
"""
@app.route("/register",methods=["GET","POST"])
def register():
    cursor = mysql.get_db().cursor()
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        salt = b"brofist"
        password = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=salt,
            iterations=100
        )
        password = password.hex()

        cursor.execute("insert into user (username,password) values (%s,%s)", (username,password))

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
@app.route("/login",methods=["GET","POST"])
def login():
    cursor = mysql.get_db().cursor()

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        salt = b"brofist"
        password = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=salt,
            iterations=100
        )
        password = password.hex()

        selectedCount = cursor.execute("select username,password from user where username=%s and password=%s",(username,password))
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
