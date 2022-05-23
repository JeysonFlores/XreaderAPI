from itsdangerous import json
from xreader.server import app, token_required, logger
from xreader.server import db, User, Novel, novel_schema, novels_schema
from flask import request, jsonify
from flask_restful import abort


@app.route("/API/novels/search", methods=["GET"])
@token_required
def search_novels():
    query = request.args.get("query")
    queried_novels = Novel.query.filter(Novel.name.like("%" + query + "%")).all()
    result = novels_schema.dump(queried_novels)

    return jsonify({"novels": result})


@app.route("/API/novels/recent", methods=["GET"])
@token_required
def recent_novels():
    novels = Novel.query.order_by(Novel.id.desc()).limit(5).all()

    result = novels_schema.dump(novels)

    return jsonify({"novels": result})


@app.route("/API/novels", methods=["GET"])
@token_required
def get_novels():
    try:
        all_novels = Novel.query.all()
        result = novels_schema.dump(all_novels)

        return jsonify({"novels": result})
    except Exception as e:
        logger.error("There was an error in querying the novels")
        abort(500)


@app.route("/API/novels/<id>", methods=["GET"])
@token_required
def get_novel(id):
    try:
        novel = Novel.query.get(id)

        if novel:
            return novel_schema.jsonify(novel)

        return jsonify({"error": "There's not novel that matches the given id."})
    except Exception as e:
        logger.error("There was an error in querying a novel")
        abort(500)
