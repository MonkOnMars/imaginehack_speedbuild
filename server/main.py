from flask import Flask, jsonify, abort, request, render_template

import secrets

app = Flask(__name__)


"""
Main page for displaying information of this website,
who are we, what we do, what you can do...
"""


@app.route("/")
def index():
    return "Main page"


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
            "lvlSeed": secrets.token_hex(nbytes=16), # the obstacle can be generated using these seed
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
        host="localhost",
        port="3333",
        debug=True
    )
