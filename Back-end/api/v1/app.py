#!/usr/bin/python3
"""Contains the https code messages handlers"""
from flask import Flask, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_mongoengine import MongoEngine
from flask_cors import CORS
import secrets
from api.v1.views import app_views
from database import UserInfo


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = MongoEngine()
app.config["MONGODB_SETTINGS"] = {
                                  "db": "ency_db",
                                  "host": "localhost",
                                  "port": 27017,
                                  }
app.register_blueprint(app_views)

# Login specific
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "app_views.login" # The login page
app.secret_key = secrets.token_hex(16)



@app.errorhandler(404)
def not_found(_):
    """404 page loader"""
    not_found = {"Error": "Page not found! Please check the URL"}
    return jsonify(not_found), 404


@login_manager.user_loader
def load_user(user_id):
    return UserInfo.find_by_id(user_id)


if __name__ == "__main__":
    """Starts the API"""
    app.run(debug=True)
