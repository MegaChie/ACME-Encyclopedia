#!/usr/bin/python3
"""Contains the https code messages handlers"""
from flask import Flask
from flask import jsonify
from flask_session import Session
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
from flask_cors import CORS
import logging
from os import getenv
import secrets
from urllib.parse import quote_plus
from datetime import timedelta
from database import UserInfo
from authlib.integrations.flask_client import OAuth


# Initialize the OAuth object
oauth = OAuth()

github = oauth.register(
    name='github',
    client_id='Ov23lirRhAXY9LeFYiUO',
    client_secret='20351d50e422c9334f1f2f9b82099afd7c77962f',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


logging.basicConfig(filename='run_logs.log',
                    level=logging.INFO)

# Run log



app = Flask(__name__)
oauth.init_app(app)

from api.v1.views import app_views
app.register_blueprint(app_views)




cors = CORS(app, resources={r"/api/*": {"origins": "*"}},
            supports_credentials=True)
db = MongoEngine()

# Check if using internet or local data base.
# Make sure to save "name" and "password" invironment variables.
if getenv("name") and getenv("password"):
    user = quote_plus(getenv("name"))
    password = quote_plus(getenv("password"))
    host = ("mongodb+srv://{}:{}@cluster0.dmcy0ry".format(user,password) +
            ".mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
else:
    host = None
app.config["MONGODB_SETTINGS"] = {
    "db": "ency_db",
    "host": host or "localhost",
    "port": 27017,
}


db.init_app(app)

# Login specific
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "app_views.login"  # The login page
app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config["SESSION_COOKIE_NAME"] = "Auth"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = False
app.config["SESSION_COOKIE_PATH"] = "/api/"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=8)
app.config["SESSION_TYPE"] = "mongodb"
app.config["SESSION_MONGODB"] = MongoClient(host or "localhost",
                                            27017)
app.config["SESSION_MONGODB_DB"] = "flask_session"
app.config["SESSION_MONGODB_COLLECT"] = "sessions"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
Session(app)

translate_API = getenv("translate_API") or "http://localhost:5000/translate"


@app.errorhandler(404)
def not_found(_):
    """404 page loader"""
    not_found = {"Error": "Page not found! Please check the URL"}
    return jsonify(not_found), 404


@login_manager.user_loader
def load_user(user_id):
    """loads a user """
    return UserInfo.find_by_id(user_id)

#for rule in app.url_map.iter_rules():
 #   print(f"{rule} -> {rule.methods}")

if __name__ == "__main__":
    """Starts the API"""
    app.run(debug=True, host="0.0.0.0")
