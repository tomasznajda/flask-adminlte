from flask_admin._compat import as_unicode
from flask_admin import Admin
from flask_security import SQLAlchemyUserDatastore
from .models import admin_db, User, Role
from .views import AdminsView
import hashlib
import urllib

admins_store = SQLAlchemyUserDatastore(admin_db, User, Role)


class AdminLte(Admin):
    """
            Collection of the admin views. Also manages menu structure.
        """

    def __init__(self, app = None, name = None, url = None, subdomain = None, index_view = None,
                 translations_path = None, endpoint = None, static_url_path = None, base_template = None,
                 category_icon_classes = None, short_name = None, long_name = None,
                 skin = 'blue'):
        super(AdminLte, self).__init__(app, name, url, subdomain, index_view, translations_path, endpoint,
                                       static_url_path, base_template, 'bootstrap3', category_icon_classes)
        self.short_name = short_name or name
        self.long_name = long_name or name
        self.skin = skin

        admin_db.app = app
        admin_db.init_app(app)
        self.add_view(AdminsView(User, admin_db.session, name = "Adminstrators", menu_icon_value = 'fa-user-secret'))

    def gravatar_image_url(self, email, default_url, size = 96):
        return "https://www.gravatar.com/avatar/" \
               + hashlib.md5(email.lower()).hexdigest() \
               + "?" + urllib.urlencode({'d': default_url, 's': str(size)})

    def set_category_icon(self, name, icon_value, icon_type = "fa"):
        cat_text = as_unicode(name)
        category = self._menu_categories.get(cat_text)

        if category is not None:
            category.icon_type = icon_type
            category.icon_value = icon_value
