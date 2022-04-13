import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from fastlogging import LogInit
import datetime
import json


logger = LogInit(pathName="./tmp/logs.log", console=True, colors=True)

with open("src/config/config.json") as json_data_file:
    cfg = json.load(json_data_file)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+cymysql://"
    + cfg["database"]["user"]
    + ":"
    + cfg["database"]["password"]
    + "@"
    + cfg["database"]["host"]
    + "/"
    + cfg["database"]["name"]
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TURN_ON_TIME"] = datetime.datetime.utcnow()
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)


db = SQLAlchemy(app)
ma = Marshmallow(app)


from models.novel import *
from models.user import *
from models.volume import *

from schemas.novel import *
from schemas.user import *
from schemas.volume import *


novel_schema = NovelSchema()
novels_schema = NovelSchema(many=True)
volume_schema = VolumeSchema()
volumes_schema = VolumeSchema(many=True)


try:
    db.create_all()
except Exception as e:
    logger.error(str(e))


from routes.API.errors import *
from routes.API.middleware import *
from routes.API.user import *
from routes.API.novel import *
from routes.API.volume import *


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
