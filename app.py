from flask import Flask, url_for
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password
from flask_admin import helpers as admin_helpers
from adminlte.admin import AdminLte

from flask_admin import menu

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

admin = AdminLte(app, name = 'FlaskCMS', skin = 'green',
                 short_name = "<b>F</b>C", long_name = "<b>Flask</b>CMS")

admin.add_view(RoleView(Role, db.session, name = "Roles", category = 'Users', menu_icon_value = 'fa-server', menu_icon_type = 'fa'))
admin.add_view(UserView(User, db.session, name = "Users", category = 'Users', menu_icon_value = 'fa-users', menu_icon_type = 'fa'))
admin.add_view(MessageView(Message, db.session, name = "Messages", menu_icon_value = 'fa-envelope', menu_icon_type = 'fa'))
admin.add_view(DeviceView(Device, db.session, name = "Devices", menu_icon_value = 'fa-laptop', menu_icon_type = 'fa'))

admin.add_link(menu.MenuLink(name='Website', category='Author', url='http://tomasznajda.com', icon_value = 'fa-globe',icon_type = 'fa', target = "_blank", ))
admin.add_link(menu.MenuLink(name='GitHub', category='Author', url='https://github.com/tomasznajda', icon_value = 'fa-github', icon_type = 'fa', target = "_blank", ))

admin.set_category_icon(name='Users', icon_type = 'fa', icon_value = 'fa-users')
admin.set_category_icon(name='Author', icon_type = 'fa', icon_value = 'fa-address-card')


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
