from __main__ import app
from flask import jsonify


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Invalid request"})


@app.errorhandler(403)
def unauthorized_request(e):
    return jsonify({"error": "Unauthorized request"})


@app.errorhandler(404)
def unknown_route(e):
    return jsonify({"error": "Invalid route"})


@app.errorhandler(405)
def invalid_method(e):
    return jsonify({"error": "Invalid method"})
