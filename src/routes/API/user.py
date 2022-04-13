from __main__ import app, token_required, logger
from __main__ import db, User
import json
from flask import request, jsonify
from flask_restful import abort
from hashlib import md5
import datetime
import jwt


@app.route("/login")
def login():
    try:
        username = request.json["name"]
        password = request.json["password"]

        user = User.query.filter_by(
            username=username, password=str(md5(password.encode("utf-8")).hexdigest())
        ).first()

        if not user:
            abort(400)

        if user.token != None:
            return jsonify({"error": "User already logged"})

        token = jwt.encode(
            {"id": user.id, "username": user.password}, app.config["SECRET_KEY"]
        )
        user.loging_in(token)
        db.session.commit()

        return jsonify({"token": token})
    except:
        abort(500)


@app.route("/signup", methods=["POST"])
def signup():
    try:
        username = request.json["username"]
        name = request.json["name"]
        password = request.json["password"]

        possible_user = User.query.filter_by(username=username).first()

        if possible_user:
            abort(400)

        new_user = User(username, name, str(md5(password.encode("utf-8")).hexdigest()))
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered"})
    except:
        abort(500)


@app.route("/logout")
@token_required
def logout():
    try:
        token = request.args.get("token")

        data = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")

        user = User.query.filter_by(id=data["id"]).first()

        if not user:
            return jsonify({"error": "User is not logged"})

        user.loging_out()
        db.session.commit()

        return jsonify({"message": "Logged out successfully"})
    except:
        abort(500)
