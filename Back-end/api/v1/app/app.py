#!/usr/bin/python3
"""Contains the https code messages handlers"""
from flask import Flask
from flask import jsonify
from flask_session import Session
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
from flask_cors import CORS
from os import getenv
import secrets
from datetime import timedelta
from database import UserInfo
from api.v1.app import oauth
app = Flask(__name__)
app.secret_key = "your_secret_key"
oauth.init_app(app)

from api.v1.views import app_views
app.register_blueprint(app_views)



cors = CORS(app, resources={r"/api/*": {"origins": "*"}},
            supports_credentials=True)
db = MongoEngine()
app.config["MONGODB_SETTINGS"] = {
    "db": "ency_db",
    "host": getenv("ip") or "localhost",
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
app.config["SESSION_MONGODB"] = MongoClient(getenv("ip") or "localhost",
                                            27017)
app.config["SESSION_MONGODB_DB"] = "flask_session"
app.config["SESSION_MONGODB_COLLECT"] = "sessions"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
Session(app)


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
