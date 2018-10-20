from flask import Flask, url_for
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password
from flask_admin import helpers as admin_helpers
import flask_admin

from flask_admin import menu

from util.gravatar import gravatar_image_url

from models import db
from models.role import Role
from models.user import User
from models.message import Message
from models.device import Device

from views.role import RoleView
from views.user import UserView
from views.message import MessageView
from views.device import DeviceView

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
db.app = app
migrate = Migrate(app, db)

user_store = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_store)

admin = flask_admin.Admin(app, name = 'FlaskCMS', template_mode = 'bootstrap3')

admin.add_view(RoleView(Role, db.session, menu_icon_type = 'fa', menu_icon_value = 'fa-server', name = "Roles", category = 'Users'))
admin.add_view(UserView(User, db.session, menu_icon_type = 'fa', menu_icon_value = 'fa-users', name = "Users", category = 'Users'))
admin.add_view(MessageView(Message, db.session, menu_icon_type = 'fa', menu_icon_value = 'fa-envelope', name = "Messages"))
admin.add_view(DeviceView(Device, db.session, menu_icon_type = 'fa', menu_icon_value = 'fa-laptop', name = "Devices"))

admin.add_link(menu.MenuLink(name='Website', url='http://tomasznajda.com', target = "_blank", category='Author'))
admin.add_link(menu.MenuLink(name='GitHub', url='https://github.com/tomasznajda', target = "_blank", category='Author'))

app.jinja_env.globals.update(gravatar_image_url = gravatar_image_url)


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        h = admin_helpers,
        get_url = url_for
    )


@app.cli.command()
def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    db.drop_all()
    db.create_all()

    with app.app_context():
        super_admin_role = Role(name = 'superadmin')
        admin_role = Role(name = 'admin')
        user_role = Role(name = 'user')
        db.session.add(super_admin_role)
        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.commit()

        test_user = user_store.create_user(
            first_name = 'John',
            last_name = 'Doe',
            email = 'admin@admin.com',
            password = encrypt_password('admin'),
            roles = [super_admin_role, admin_role]
        )
        db.session.add(test_user)
        db.session.commit()
    return


if __name__ == '__main__':
    app.run()
