from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin

admin_db = SQLAlchemy()

roles_users = admin_db.Table(
    'roles_users',
    admin_db.Column('user_id', admin_db.Integer(), admin_db.ForeignKey('user.id')),
    admin_db.Column('role_id', admin_db.Integer(), admin_db.ForeignKey('role.id'))
)


class Role(admin_db.Model, RoleMixin):
    id = admin_db.Column(admin_db.Integer(), primary_key = True)
    name = admin_db.Column(admin_db.String(80), unique = True)
    description = admin_db.Column(admin_db.String(255))

    def __str__(self):
        return self.name


class User(admin_db.Model, UserMixin):
    id = admin_db.Column(admin_db.Integer, primary_key = True)
    first_name = admin_db.Column(admin_db.String(255))
    last_name = admin_db.Column(admin_db.String(255))
    email = admin_db.Column(admin_db.String(255), unique = True, nullable = False)
    password = admin_db.Column(admin_db.String(255), nullable = False)
    active = admin_db.Column(admin_db.Boolean(), nullable = False)
    roles = admin_db.relationship('Role', secondary = roles_users, backref = 'users')

    def __str__(self):
        return self.first_name + " " + self.last_name + " <" + self.email + ">"