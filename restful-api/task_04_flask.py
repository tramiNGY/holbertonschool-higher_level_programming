#!/usr/bin/python3
'''
This module contains simple API using Python Flask
'''
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


all_users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"}
}


@app.route("/data")
def data():
    userlist = []
    for key in all_users:
        userlist.append(key)
    return jsonify(userlist)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def users(username):
    if username in all_users:
        return jsonify(all_users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    if "username" not in new_user:
        return ({"error": "Username is required"}), 400

    all_users[new_user["username"]] = {
        "username": new_user["username"],
        "name": new_user["name"],
        "age": new_user["age"],
        "city": new_user["city"]
    }
    return jsonify({
        "message": "User added",
        "user": all_users[new_user["username"]]
    }), 201


if __name__ == "__main__":
    app.run(port=5000)
