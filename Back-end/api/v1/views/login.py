#!/usr/bin/python3
"""Contains the auth of the API"""

from api.v1.views import app_views
from flask import jsonify, request, session, url_for
from flask_login import login_user, logout_user, login_required, current_user
from database import UserInfo
from api.v1.app import oauth

# Set the redirect URI for GitHub (should match what you registered on GitHub)
github_redirect_uri = 'http://localhost:5000/api/v1/auth/github/callback'
google_redirect_uri = 'http://localhost:5000/api/v1/auth/google/callback'


@app_views.route('/login/github')
def login_github():
    github = oauth.github()
    redirect_uri = url_for('login.login_github_callback', _external=True)
    return github.authorize(github_redirect_uri=redirect_uri)


@app_views.route('auth/github/callback')
def login_github_callback():
    github = oauth.github()
    token = github.authorize_access_token()
    user_info = github.get('user').json()
    user_email = github.get('user/emails').json()[0]['email']
    user_name = user_info['login']
    session['github_token'] = token
    existing_user = UserInfo.find_by_email(user_email)
    if existing_user:
        session['_user_id'] = str(existing_user.id)
        return jsonify({'user_id': str(existing_user.id)}), 200

    # if user doesn't exist create new one
    new_user = UserInfo(username=user_name, email=user_email)
    new_user.authed = True
    new_user.add_to_coll()
    session['_user_id'] = str(new_user.id)
    return jsonify({'user_id': str(new_user.id)}), 200


@app_views.route('/login/google')
def login_google_oauth():
    google = oauth.google()
    redirect_uri = url_for('login.login_google_oauth_callback', _external=True)
    return google.authorize(google_redirect_uri=redirect_uri)


@app_views.route('/login/google/callback')
def login_google_oauth_callback():
    google = oauth.google()
    token = google.authorize_access_token()
    user_info = google.get('user').json()
    user_email = user_info['email']
    user_name = user_info['login']
    if user_info is None or token is None:
        return jsonify({'error': 'Access denied'}), 403
    session['google_token'] = token
    existing_user = UserInfo.find_by_email(user_name)
    if existing_user:
        session['_user_id'] = str(existing_user.id)
        return jsonify({'user_id': str(existing_user.id)}), 200
    new_user = UserInfo(username=user_name, email=user_email)
    new_user.authed = True
    new_user.add_to_coll()
    session['_user_id'] = str(new_user.id)
    return jsonify({'user_id': str(new_user.id)}), 200


@app_views.route("/login", methods=["POST"], strict_slashes=False)
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
            from api.v1.app.app import app
            app.logger.info(f"User {user.id} logged in, session ID: {session['_user_id']}")
            if current_user.is_authenticated:
                print("User is authenticated")
            else:
                print("User is not authenticated")

            logged = {"Status": "Logged in!"}
            # return redirect(url_for('dashboard'))
            return jsonify(logged), 201
        # Add login page
        # return redirect(url_for('login.login'))

    not_json = {"Error": "Not a JSON"}
    return jsonify(not_json), 400


@app_views.route("/logout", methods=["GET"])
def logout():
    print(session)
    if not current_user.is_authenticated:
        print(current_user)
        return jsonify({"Error": "Not authenticated"}), 401
    logout_user()
    loged_out = {"Status": "Logged out! Please Sign in again"}
    return jsonify(loged_out), 201
    # return redirect(url_for('login'))
