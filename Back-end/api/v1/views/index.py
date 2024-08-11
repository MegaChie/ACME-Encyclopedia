#!/usr/bin/python3
"""Contains the status of the API"""
from api.v1.views import app_views
from flask import jsonify
from database import UserInfo


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def api_status():
    """Returns an indicator of the API status"""
    good_state = {"Status": "API running!"}
    return jsonify(good_state), 200


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def api_stats():
    """Returns the number of users and materials"""
    user_count = UserInfo.objects.count()
    stats = {"Users": user_count}
    return jsonify(stats), 200
