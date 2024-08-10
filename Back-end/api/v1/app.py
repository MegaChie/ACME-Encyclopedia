#!/usr/bin/python3
""" Flask Application """
from flask import Flask, jsonify, request
from flask_cors import CORS
from api.v1.views import app_views, app_views_docs


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found():
    """404 page loader"""
    return jsonify({"Error": "Page not found! Please check the URL"}), 404


if __name__ == "__main__":
    """Starts the API"""
    app.run(debug=True)
