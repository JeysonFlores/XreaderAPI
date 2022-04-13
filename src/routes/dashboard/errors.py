from __main__ import app, request, render_template


@app.route("/error")
def generic_error():
    message = request.args.get("message", type=str)
    if not message:
        message = ""
    return render_template("error.html", message=message)
