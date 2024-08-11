#!/usr/bin/python3
"""Contains the users haneling endpoints"""
from api.v1.views import app_views
from flask import jsonify, request
from database import UserInfo


@app_views.route("/add_users", methods=["POST"], strict_slashes=False)
def add_user():
    """Adds a new user to the database"""
    if request.is_json:
        data = request.get_json()
        if len(data.keys()) != 2:
            missing = {"Error": "Missing data"}
            return jsonify(missing), 400

        new_user = UserInfo(username=data.get("username"),
                            email=data.get("email"))
        new_user.add_to_coll()
        return jsonify(new_user.to_json()), 200

    else:
        not_json = {"Error": "Not a JSON"}
        return jsonify(not_json), 400
        
