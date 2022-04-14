from __main__ import app, session_required
from __main__ import db, Novel, Volume

from flask import render_template


@app.route("/admin/novels/<novel_id>/volumes")
@session_required
def dashboard_novel_volumes(novel_id):
    novel = Novel.query.get(novel_id)

    all_volumes = Volume.query.filter_by(id_novel=novel_id).all()

    return render_template(
        "dashboard_volumes.html", volumes=all_volumes, main_novel=novel, len=len
    )
