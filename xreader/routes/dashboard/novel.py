from xreader.server import app, session_required, request
from xreader.server import db, Novel

from flask import redirect, render_template


@app.route("/admin/novels")
@session_required
def dashboard_novels():
    novels = Novel.query.all()

    return render_template("dashboard_novels.html", novels=novels, len=len)


@app.route("/admin/novels/add", methods=["GET", "POST"])
@session_required
def dashboard_novels_add():
    if request.method == "POST":
        name = request.form.get("nameField")
        author = request.form.get("authorField")
        image_path = request.form.get("imagepathField")
        publishing_year = request.form.get("publishingField")
        description = request.form.get("descriptionField")

        new_novel = Novel(name, description, author, image_path, int(publishing_year))

        db.session.add(new_novel)
        db.session.commit()

        return redirect("/admin/novels")

    return render_template("dashboard_novels_add.html")


@app.route("/admin/novels/<id>/edit", methods=["GET", "POST"])
@session_required
def dashboard_novel_edit(id):
    novel = Novel.query.get(id)

    if not novel:
        return redirect("/error?message=There's no novel that matches the given id.")

    if request.method == "POST":
        name = request.form.get("nameField")
        author = request.form.get("authorField")
        image_path = request.form.get("imagepathField")
        publishing_year = request.form.get("publishingField")
        description = request.form.get("descriptionField")

        novel.name = name
        novel.author = author
        novel.image_path = image_path
        novel.publishing_year = int(publishing_year)
        novel.description = description

        db.session.commit()

        return redirect("/admin/novels")

    return render_template("dashboard_novels_edit.html", novel=novel)


@app.route("/admin/novels/<id>/delete")
@session_required
def dashboard_novel_delete(id):
    novel = Novel.query.get(id)

    if not novel:
        return redirect("/error?message=There's no novel that matches the given id.")

    db.session.delete(novel)
    db.session.commit()

    return redirect("/admin/novels")
