from __main__ import db


class Novel(db.Model):
    __tablename__ = "novels"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    publishing_year = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    volumes = db.relationship("Volume", backref="volumes", lazy=True)

    def __init__(self, name: str, author: str, publishing_year: int):
        self.name = name
        self.author = author
        self.publishing_year = publishing_year
        self.status = True

    def deactivate(self):
        self.status = False
