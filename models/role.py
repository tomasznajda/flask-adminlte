from . import db
from flask_security import RoleMixin


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name
