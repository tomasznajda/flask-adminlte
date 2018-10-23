from flask import Flask, url_for
from flask_migrate import Migrate
from flask_security import Security
from flask_security.utils import encrypt_password
from flask_admin import helpers as admin_helpers
from adminlte.admin import AdminLte, admins_store, admin_db
from adminlte.models import Role
from adminlte.views import FaLink

from flask_admin import menu

from models import db
from models.message import Message
from models.device import Device

from views.message import MessageView
from views.device import DeviceView

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
db.app = app
migrate = Migrate(app, db)
admin_migrate = Migrate(app, admin_db)

security = Security(app, admins_store)
admin = AdminLte(app, skin = 'green', name = 'FlaskCMS', short_name = "<b>F</b>C", long_name = "<b>Flask</b>CMS")

admin.add_view(MessageView(Message, db.session, name = "Messages", menu_icon_value = 'fa-envelope'))
admin.add_view(DeviceView(Device, db.session, name = "Devices", menu_icon_value = 'fa-laptop'))

admin.add_link(FaLink(name = 'Website', category = 'Author', url = 'http://tomasznajda.com',
                      icon_value = 'fa-globe', target = "_blank"))
admin.add_link(FaLink(name = 'GitHub', category = 'Author', url = 'https://github.com/tomasznajda',
                      icon_value = 'fa-github', target = "_blank"))

admin.set_category_icon(name = 'Author', icon_value = 'fa-address-card')


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

    admin_db.drop_all()
    admin_db.create_all()

    with app.app_context():
        super_admin_role = Role(name = 'superadmin')
        admin_role = Role(name = 'admin')
        admin_db.session.add(super_admin_role)
        admin_db.session.add(admin_role)
        admin_db.session.commit()

        test_user = admins_store.create_user(
            first_name = 'John',
            last_name = 'Doe',
            email = 'admin@admin.com',
            password = encrypt_password('admin'),
            roles = [super_admin_role, admin_role]
        )
        admin_db.session.add(test_user)
        admin_db.session.commit()
    return


if __name__ == '__main__':
    app.run()
