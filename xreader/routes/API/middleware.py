from xreader.server import app
from flask import request
from flask_restful import abort
from functools import wraps
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        print(token)
        if not token:
            # return jsonify({"error": "1", "message":"token is missing"}), 403
            abort(403)
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
        except:
            # return jsonify({"error": "1", "message": "token is invalid"}), 403
            abort(403)
        return f(*args, **kwargs)

    return decorated
