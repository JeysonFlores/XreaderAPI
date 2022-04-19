from xreader.server import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    permissions = db.Column(db.Integer)
    token = db.Column(db.Text)

    def __init__(self, username: str, name: str, password: str):
        self.username = username
        self.name = name
        self.password = password
        self.permissions = 0

    def loging_in(self, token: str):
        self.token = token

    def loging_out(self):
        self.token = None
