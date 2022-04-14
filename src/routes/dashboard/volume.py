from __main__ import app, session_required, request
from __main__ import db, Novel, Volume
from email.mime import image

from flask import render_template, redirect


@app.route("/admin/novels/<novel_id>/volumes")
@session_required
def dashboard_novel_volumes(novel_id):
    novel = Novel.query.get(novel_id)

    all_volumes = Volume.query.filter_by(id_novel=novel_id).all()
    
    return render_template("dashboard_volumes.html", volumes=all_volumes, main_novel=novel, len=len)


@app.route("/admin/novels/<novel_id>/volumes/add", methods=["GET", "POST"])
@session_required
def dashboard_novel_volumes_add(novel_id):
    novel = Novel.query.get(novel_id)

    if not novel:
        return redirect("/error?message=There's no novel that matches the given id.")

    if request.method == "POST":
        name = request.form.get("nameField")
        link = request.form.get("linkField")
        image_path = request.form.get("imagepathField")

        new_volume = Volume(name, link, image_path, int(novel_id))

        db.session.add(new_volume)
        db.session.commit()

        return redirect("/admin/novels/" + str(novel_id) + "/volumes")

    return render_template("dashboard_volumes_add.html", novel=novel)


@app.route("/admin/novels/<novel_id>/volumes/<volume_id>/edit", methods=["GET", "POST"])
@session_required
def dashboard_novels_volumes_edit(novel_id, volume_id):
    novel = Novel.query.get(novel_id)
    volume = Volume.query.get(volume_id)

    if not novel:
        return redirect("/error?message=There's no novel that matches the given id.")

    if not volume:
        return redirect("/error?message=There's no volume that matches the given id.")

    if request.method == "POST":
        name = request.form.get("nameField")
        link = request.form.get("linkField")
        image_path = request.form.get("imagepathField")

        volume.name = name
        volume.link = link
        volume.image_path = image_path

        db.session.commit()

        return redirect("/admin/novels/" + str(novel_id) + "/volumes")

    return render_template("dashboard_volumes_edit.html", novel=novel, volume=volume)


@app.route("/admin/novels/<novel_id>/volumes/<volume_id>/delete")
@session_required
def dashboard_novels_volumes_delete(novel_id, volume_id):
    volume = Volume.query.get(volume_id)

    if not volume:
        return redirect("/error?message=There's no volume that matches the given id.")

    db.session.delete(volume)
    db.session.commit()

    return redirect("/admin/novels/" + str(novel_id) + "/volumes")

@app.route("/admin/volumes/<id>/delete")
@session_required
def dashboard_volumes_delete(id):
    volume = Volume.query.get(id)

    if not volume:
        return redirect("/error?message=There's no volume that matches the given id.")

    db.session.delete(volume)
    db.session.commit()

    return redirect("/admin")