#!/usr/bin/python3
"""Contains the auth of the API"""
from api.v1.views import app_views
from flask import jsonify, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from database import UserInfo


@app_views.route("/login_users", methods=["POST"], strict_slashes=False)
def login():
    """Login a user while directing new one to signup"""
    if request.is_json:
        try:
            email = request.get_json().get("email")
            username = request.get_json().get("username")
            password = request.get_json().get("password")
        except Exception:
            missing = {"Error": "Missing data"}
            return jsonify(missing), 400

        user = UserInfo.objects(email=email,
                                username=username).first()
        if not user:
            no_user = {"Error": "User not found"}
            return jsonify(no_user), 400

        if user.is_password(password):
            login_user(user)
            from api.v1.app import app
            from flask import session
            app.logger.info(f"User {user.id} logged in, session ID: {session['_user_id']}")
            if current_user.is_authenticated:
                print("User is authenticated")
            else:
                print("User is not authenticated")
            logged = {"Status": "Loged in!"}
            # return redirect(url_for('dashboard'))
            return jsonify(logged), 201
        # Add login page
        # return redirect(url_for('login.login'))

    not_json = {"Error": "Not a JSON"}
    return jsonify(not_json), 400


@app_views.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    loged_out = {"Status": "Logged out! Please Sign in again"}
    return jsonify(loged_out), 201
    # return redirect(url_for('login'))
