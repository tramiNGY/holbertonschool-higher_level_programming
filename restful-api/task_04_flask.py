#!/usr/bin/python3
'''
This module contains simple API using Python Flask
'''
from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


@app.route("/")
def home():
    """Displays home message"""
    return "Welcome to the Flask API!"


all_users = {}


@app.route("/data")
def data():
    """Returns username list"""
    return jsonify(list(all_users.keys()))


@app.route("/status")
def status():
    """Returns OK status if no error"""
    return "OK"


@app.route("/users/<username>")
def users(username):
    """Returns user data"""
    if username in all_users:
        user_data = all_users[username]
        return app.response_class(
            json.dumps(user_data, indent=4, sort_keys=False),
            content_type='application/json'
        )
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds new user data and returns it"""
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return ({"error": "Username is required"}), 400

    all_users[username] = new_user
    response = {
        "message": "User added",
        "user": all_users[new_user["username"]]
    }

    return app.response_class(
        json.dumps(response, indent=4, sort_keys=False),
        content_type='application/json'
    ), 201


if __name__ == "__main__":
    app.run(debug=True)
