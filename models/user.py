from . import db
from flask_security import UserMixin

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    active = db.Column(db.Boolean(), nullable = False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary = roles_users, backref = db.backref('users', lazy = 'dynamic'))

    def __str__(self):
        return self.first_name + " " + self.last_name + " <" + self.email + ">"
