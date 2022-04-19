from functools import wraps
from flask import redirect, session


def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "username" not in session:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated


def no_session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "username" in session:
            return redirect("/admin")
        return f(*args, **kwargs)

    return decorated
