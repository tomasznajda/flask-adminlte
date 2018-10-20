from . import db


class Device(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum("android", "ios"), nullable=False)
    rooted = db.Column(db.Boolean, nullable=False)
