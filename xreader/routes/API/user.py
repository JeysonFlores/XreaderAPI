from xreader.server import app, token_required, logger
from xreader.server import db, User
from flask import request, jsonify
from flask_restful import abort
from hashlib import md5
import jwt


@app.route("/API/login")
def api_login():
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
        logger.error("There was an error logging in")
        abort(500)


@app.route("/API/signup", methods=["POST"])
def api_signup():
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
        logger.error("There was an error signing up")
        abort(500)


@app.route("/API/logout")
@token_required
def api_logout():
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
        logger.error("There was an error logging out")
        abort(500)

@app.route("/API/setadmin")
def set_admin():
    possible_admin = User.query.filter_by(id=1).first()

    if possible_admin:
        abort(400)

    new_admin = User("mainDev", "Fernando Murrieta", str(md5("12345".encode("utf-8")).hexdigest()))
    new_admin.permissions = 1

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({ "message": "Admin registered"})