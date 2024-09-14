#!/usr/bin/python3
"""Contains the status of the API"""
from api.v1.views import app_views
from flask import jsonify, request, redirect, url_for
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


@app_views.route('/documentation', methods=["GET"], strict_slashes=False)
def docs():
    """Redirects the documentation of the API"""
    url = ("https://night-belly-22c.notion.site/"
           + "API-Docs-a3ab83c49bee49f5aaa08f4b512f1b08?pvs=4")
    return redirect(url, 308)
