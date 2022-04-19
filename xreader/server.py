import secrets
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from fastlogging import LogInit
import datetime
import json


logger = LogInit(pathName="./tmp/logs.log", console=True, colors=True)

with open("xreader/config/config.json") as json_data_file:
    cfg = json.load(json_data_file)


app = Flask(__name__, template_folder="public/templates", static_folder="public/static")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://"
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


from xreader.models.novel import *
from xreader.models.user import *
from xreader.models.volume import *

from xreader.schemas.novel import *
from xreader.schemas.user import *
from xreader.schemas.volume import *


novel_schema = NovelSchema()
novels_schema = NovelSchema(many=True)
volume_schema = VolumeSchema()
volumes_schema = VolumeSchema(many=True)


try:
    db.create_all()
except Exception as e:
    logger.error(str(e))


from xreader.routes.API.errors import *
from xreader.routes.API.middleware import *
from xreader.routes.API.user import *
from xreader.routes.API.novel import *
from xreader.routes.API.volume import *

from xreader.routes.dashboard.errors import *
from xreader.routes.dashboard.middleware import *
from xreader.routes.dashboard.base import *
from xreader.routes.dashboard.novel import *
from xreader.routes.dashboard.volume import *

if __name__ == "__main__":
    app.run(debug=cfg["API"]["debug"], threaded=cfg["API"]["threaded"])
