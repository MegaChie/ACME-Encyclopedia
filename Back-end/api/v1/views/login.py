#!/usr/bin/python3
"""Contains the auth of the API"""
from api.v1.views import app_views
from flask import jsonify, request, redirect, url_for, Blueprint, session
from flask_login import login_user, logout_user, login_required, current_user
from database import UserInfo
from flask_oauthlib.client import OAuth

oauth = OAuth()

# github config

github = oauth.remote_app(
    'github',
    consumer_key='YOUR_GITHUB_CLIENT_ID',
    consumer_secret='YOUR_GITHUB_CLIENT_SECRET',
    request_token_params={
        'scope': 'user:email',
    },
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

# Set the redirect URI for GitHub (should match what you registered on GitHub)
github_redirect_uri = 'http://localhost:5000/api/v1/auth/github/callback'

google = oauth.remote_app(
    'google',
    consumer_key='YOUR_GOOGLE_CLIENT_ID',
    consumer_secret='YOUR_GOOGLE_CLIENT_SECRET',
    request_token_params={
        'scope': 'email profile',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)
google_redirect_uri = 'http://localhost:5000/api/v1/auth/google/callback'


@app_views.route('/login/github')
def login_github():
    return github.authorize(github_redirect_uri=github_redirect_uri)


@app_views.route('auth/github/callback')
def login_github_callback():
    response = github.authorized_response()
    if response is None or 'access_token' not in response:
        return jsonify({'error': 'Access denied'}), 403
    session['github_token'] = (response.get('access_token'), '')
    user_name = github.get('user').get('login')
    emails = github.get('user/emails').data
    primary_email = next(email['email'] for email in emails if email['primary'])

    existing_user = UserInfo.find_by_email(primary_email)
    if existing_user:
        session['user_id'] = str(existing_user.id)
        return jsonify({'user_id': str(existing_user.id)}), 200

    # if user doesn't exist create new one
    new_user = UserInfo(username=user_name, email=primary_email)
    new_user.authed = True
    new_user.add_to_coll()
    session['user_id'] = str(new_user.id)
    return jsonify({'user_id': str(new_user.id)}), 200


@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')


@app_views.route('/login/google')
def login_google_oauth():
    return google.authorize(google_redirect_uri=google_redirect_uri)


@app_views.route('/login/google/callback')
def login_google_oauth_callback():
    response = google.authorized_response()
    if response is None or 'access_token' not in response:
        return jsonify({'error': 'Access denied'}), 403
    session['google_token'] = (response.get('access_token'), '')
    user_name = google.get('user').get('login')
    user_info = google.get('userinfo').data
    existing_user = UserInfo.find_by_email(user_name)
    if existing_user:
        session['user_id'] = str(existing_user.id)
        return jsonify({'user_id': str(existing_user.id)}), 200
    new_user = UserInfo(username=user_name, email=user_info['email'])
    new_user.authed = True
    new_user.add_to_coll()
    session['user_id'] = str(new_user.id)
    return jsonify({'user_id': str(new_user.id)}), 200


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


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
