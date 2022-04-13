from __main__ import app, token_required, logger
from __main__ import db, User, Volume, volume_schema, volumes_schema
from flask import request, jsonify
from flask_restful import abort


@app.route("/API/novels/<id>/volumes", methods=["GET"])
def get_volumes(id):
    try:
        all_volumes = Volume.query.filter_by(id_novel=id).all()
        result = volumes_schema.dump(all_volumes)

        return jsonify({"volumes": result})
    except Exception as e:
        abort(500)


@app.route("/API/volumes/<id>", methods=["GET"])
def get_volume(id):
    try:
        volume = Volume.query.get(id)

        if volume:
            return volume_schema.jsonify(volume)

        return jsonify({"error": "There's no volume that matches the given id."})
    except Exception as e:
        abort(500)
