#!/usr/bin/python3
"""Contains the https code messages handlers"""
from flask import Flask
from flask import jsonify
from flask_cors import CORS



app = Flask(__name__)
cors = CORS(app, supports_credentials=True)

@app.route("/test", strict_slashes=False)
def test():
    """Temp API endpoint"""
    good = {"Status": "Good"}
    return jsonify(good)


if __name__ == "__main__":
    """Starts the API"""
    app.run(debug=True)
