#!/usr/bin/python3
"""Contains the https code messages handlers"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found():
    """404 page loader"""
    not_found = {"Error": "Page not found! Please check the URL"}
    return jsonify(not_found), 404


@app.errorhandler(500)
def server_error():
    """
    Server error page loader.
    Only for devolopers.
    """
    error_message = {"Error": "Server incountered an error. Pleses check logs"}
    return jsonify(error_message), 500


@app.route("/status", methods=["GET"], strict_slashes=False)
def api_status():
    """Checks if server is running"""
    good_state = {"Status": "API running!"}
    return jsonify(good_state), 200


if __name__ == "__main__":
    """Starts the API"""
    app.run(debug=True)
