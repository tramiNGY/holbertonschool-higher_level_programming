#!/usr/bin/python3
'''
This module contains simple API using Python Flask
'''
from flask import Flask
from flask import jsonify
from flask import request
from collections import OrderedDict

app = Flask(__name__)


@app.route("/")
def home():
    """Displays home message"""
    return "Welcome to the Flask API!"


all_users = OrderedDict({
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"}
})


@app.route("/data")
def data():
    """Returns username list"""
    userlist = []
    for key in all_users:
        userlist.append(key)
    return jsonify(userlist)


@app.route("/status")
def status():
    """Returns OK status if no error"""
    return "OK"


@app.route("/users/<username>")
def users(username):
    """Returns user data"""
    if username in all_users:
        return jsonify(all_users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds new user data and returns it"""
    new_user = request.get_json()
    if not new_user or "username" not in new_user:
        return ({"error": "Username is required"}), 400
    
    if "name" not in new_user or "city" not in new_user or "age" not in new_user:
        return jsonify({"error": "Name, age, and city are required"}), 400

    if new_user["username"] in all_users:
        return jsonify({"error": "Username already exists"}), 400

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
