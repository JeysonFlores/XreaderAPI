from __main__ import app, request, render_template
from __main__ import User, session_required, no_session_required
from flask import redirect, session
from hashlib import md5


@app.route("/admin")
@session_required
def admin_main():
    return render_template("dashboard_index.html")


@app.route("/login", methods=["GET", "POST"])
@no_session_required
def dashboard_login():
    if request.method == "POST":
        username = request.form.get("usernameField")
        password = request.form.get("passwordField")

        user = User.query.filter_by(
            username=str(username),
            password=str(md5(password.encode("utf-8")).hexdigest()),
        ).first()

        if user is not None:
            session["username"] = username

            return redirect("/admin")

        return redirect(
            "/error?message=Invalid username or password. Please check your credentials."
        )

    return render_template("login.html")


@app.route("/logout")
@session_required
def dashboard_logout():
    session.pop("username", None)
    return redirect("/login")
