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

        # Check for duplicates first
        new_user = UserInfo(username=data.get("username"),
                            email=data.get("email"))
        new_user.add_to_coll()
        return jsonify(new_user.to_json()), 201

    else:
        not_json = {"Error": "Not a JSON"}
        return jsonify(not_json), 400
        

@app_views.route("/users/<id>", methods=["GET"], strict_slashes=False)
def users(id):
    """List all users or a specific user if an ID is passed"""
    if not id:
        all_users = UserInfo.objects()
        data = []
        for user in all_users:
            temp = user.to_json()
            data.append(temp)
        
        return jsonify({"All users": data}), 200

    else:
        user = UserInfo.find_by_id(id)

        if user:
            return jsonify(user.to_json()), 200
        else:
            not_found = {"Error": "User not found"}
            return jsonify(not_found), 400


@app_views.route("/edit_user/<id>", methods=["PUT"], strict_slashes=False)
def user_edit(id):
    """Edit user information"""
    user = UserInfo.find_by_id(id)

    if user:
        if request.is_json:
            data = request.get_json()
        else:
            not_json = {"Error": "Not a JSON"}
            return jsonify(not_json), 400

        user.user_modfy(id, data)
        edited = {"Status": "User edited"}
        return jsonify(edited), 200
    else:
        not_found = {"Error": "User not found"}
        return jsonify(not_found), 400


@app_views.route("/delete_users/<id>", methods=["DELETE"],
                 strict_slashes=False)
def user_delete(id):
    """Deletes a user from database"""
    if id:
        user = UserInfo.find_by_id(id)
        if user:
            user.delete_by_id(id)
            deleted = {"Status": "Deletion done"}
            return jsonify(deleted), 201
        else:
            not_found = {"Error": "User not found"}
            return jsonify(not_found), 400
    else:
        not_deleted = {"Status": "Failed", "Reason": "No ID passed"}
        return jsonify(not_deleted), 400
