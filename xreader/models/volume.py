from xreader.server import db


class Volume(db.Model):
    __tablename__ = "volumes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    link = db.Column(db.Text)
    image_path = db.Column(db.Text)
    status = db.Column(db.Boolean)
    id_novel = db.Column(db.Integer, db.ForeignKey("novels.id"), nullable=False)

    def __init__(self, name: str, link: str, image_path: str, id_novel: int):
        self.name = name
        self.link = link
        self.image_path = image_path
        self.status = True
        self.id_novel = id_novel

    def deactivate(self):
        self.status = False
