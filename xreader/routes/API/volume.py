from xreader.server import app, token_required, logger
from xreader.server import db, User, Volume, volume_schema, volumes_schema
from flask import request, jsonify
from flask_restful import abort


@app.route("/API/novels/<id>/volumes", methods=["GET"])
@token_required
def get_volumes(id):
    try:
        all_volumes = Volume.query.filter_by(id_novel=id).all()
        result = volumes_schema.dump(all_volumes)

        return jsonify({"volumes": result})
    except Exception as e:
        logger.error("There was an error querying all volumes")
        abort(500)


@app.route("/API/novels/<novel_id>/volumes/<volume_id>", methods=["GET"])
@token_required
def get_volume_from_novel(novel_id, volume_id):
    try:
        volume = Volume.query.filter_by(id=volume_id, id_novel=novel_id).first()

        if volume:
            return volume_schema.jsonify(volume)

        return jsonify({"error": "There's no volume that matches the given id."})
    except Exception as e:
        logger.error("There was an error querying a volume")
        abort(500)


@app.route("/API/volumes/<id>", methods=["GET"])
@token_required
def get_volume(id):
    try:
        volume = Volume.query.get(id)

        if volume:
            return volume_schema.jsonify(volume)

        return jsonify({"error": "There's no volume that matches the given id."})
    except Exception as e:
        logger.error("There was an error querying a volume")
        abort(500)
