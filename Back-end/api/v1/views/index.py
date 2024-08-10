#!/usr/bin/python3
"""Contains the status of the API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def api_status():
    good_state = {"Status": "API running!"}
    return jsonify(good_state), 200
