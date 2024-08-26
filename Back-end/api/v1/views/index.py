#!/usr/bin/python3
"""Contains the status of the API"""
from api.v1.views import app_views
from flask import jsonify, request
from database import UserInfo, ArticleInfo


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def api_status():
    """Returns an indicator of the API status"""
    good_state = {"Status": "API running!"}
    return jsonify(good_state), 200


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def api_stats():
    """Returns the number of users and materials"""
    user_count = UserInfo.objects.count()
    article_count = ArticleInfo.objects.count()
    stats = {"Users": user_count, "Articles": article_count}
    return jsonify(stats), 200


@app_views.route('/check_session', methods=['GET'])
def check_session():
    from flask_login import current_user
    if current_user.is_authenticated:
        return jsonify({"Status": "Session is active", "User": current_user.username})
    else:
        return jsonify({"Status": "No active session",
                        "cookie": request.cookies.get("Auth")})


@app_views.route('/debug_session', methods=['GET'])
def debug_session():
    from flask import session
    return jsonify({"session": dict(session)})
