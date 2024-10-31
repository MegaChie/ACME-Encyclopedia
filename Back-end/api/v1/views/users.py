#!/usr/bin/python3
"""Contains the users haneling endpoints"""
from api.v1.views import app_views
from flask import jsonify, request
from flask_login import login_required
from database import UserInfo


@app_views.route("/add_users", methods=["POST"], strict_slashes=False)
def add_user():
    """Adds a new user to the database"""
    if request.is_json:
        data = request.get_json()
        if len(data) != 3:
            check_list = ["username", "email", "password"]
            missing = []
            for elem in check_list:
                if elem not in data.keys():
                    missing.append(elem)
            empty_values = {"Error": "Missing {}".format(", ".join(missing))}
            return jsonify(empty_values), 400

        name = UserInfo.find_by_name(data.get("username"))
        if name:
            used = {"Error": "this name is already used"}
            return jsonify(used), 400
        email = UserInfo.find_by_email(data.get("email"))
        if email:
            used = {"Error": "this email is already used"}
            return jsonify(used), 400

        new_user = UserInfo(username=data.get("username"),
                            email=data.get("email"),
                            password=data.get("password"))
        new_user.hash_password()
        new_user.add_to_coll()

        return jsonify(new_user.to_json()), 201

    else:
        not_json = {"Error": "Not a JSON"}
        return jsonify(not_json), 400


@app_views.route("/users/<id>", methods=["GET"], strict_slashes=False)
@app_views.route("/users", methods=["GET"], strict_slashes=False)
def users(id=None):
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
@login_required
def user_edit(id=None):
    """Edit user information"""
    user = UserInfo.find_by_id(id)

    if user:
        if request.is_json:
            data = request.get_json()
        else:
            not_json = {"Error": "Not a JSON"}
            return jsonify(not_json), 400

        user.user_modfy(id, **data)
        edited = {"Status": "User edited"}
        return jsonify(edited), 200
    else:
        not_found = {"Error": "User not found"}
        return jsonify(not_found), 404


@app_views.route("/delete_users/<id>", methods=["DELETE"],
                 strict_slashes=False)
@login_required
def user_delete(id=None):
    """Deletes a user from database"""
    if id:
        user = UserInfo.find_by_id(id)
        if user:
            user.delete_by_id(id)
            deleted = {"Status": "Deletion done"}
            return jsonify(deleted), 204
        else:
            not_found = {"Error": "User not found"}
            return jsonify(not_found), 404
    else:
        not_deleted = {"Status": "Failed", "Reason": "No ID passed"}
        return jsonify(not_deleted), 400
