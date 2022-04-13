from __main__ import app, token_required, logger
from __main__ import db, User, Novel, novel_schema, novels_schema
from flask import request, jsonify
from flask_restful import abort


@app.route("/API/novels", methods=["GET"])
def get_novels():
    try:
        all_novels = Novel.query.all()
        result = novels_schema.dump(all_novels)

        return jsonify({"novels": result})
    except Exception as e:
        abort(500)


@app.route("/API/novels/<id>", methods=["GET"])
def get_novel(id):
    try:
        novel = Novel.query.get(id)

        if novel:
            return novel_schema.jsonify(novel)

        return jsonify({"error": "There's not novel that matches the given id."})
    except Exception as e:
        abort(500)
