from flask_admin._compat import as_unicode
from flask_admin import Admin
from flask_admin.menu import MenuCategory
import hashlib
import urllib


class AdminLte(Admin):
    """
            Collection of the admin views. Also manages menu structure.
        """

    def __init__(self, app = None, name = None, url = None, subdomain = None, index_view = None,
                 translations_path = None, endpoint = None, static_url_path = None, base_template = None,
                 category_icon_classes = None, short_name = None, long_name = None,
                 skin = 'blue'):
        """
            Constructor.

            :param app:
                Flask application object
            :param name:
                Application name. Will be displayed in the main menu and as a page title. Defaults to "Admin"
            :param url:
                Base URL
            :param subdomain:
                Subdomain to use
            :param index_view:
                Home page view to use. Defaults to `AdminIndexView`.
            :param translations_path:
                Location of the translation message catalogs. By default will use the translations
                shipped with Flask-Admin.
            :param endpoint:
                Base endpoint name for index view. If you use multiple instances of the `Admin` class with
                a single Flask application, you have to set a unique endpoint name for each instance.
            :param static_url_path:
                Static URL Path. If provided, this specifies the default path to the static url directory for
                all its views. Can be overridden in view configuration.
            :param base_template:
                Override base HTML template for all static views. Defaults to `admin/base.html`.
            :param template_mode:
                Base template path. Defaults to `bootstrap2`. If you want to use
                Bootstrap 3 integration, change it to `bootstrap3`.
            :param category_icon_classes:
                A dict of category names as keys and html classes as values to be added to menu category icons.
                Example: {'Favorites': 'glyphicon glyphicon-star'}
        """
        super(AdminLte, self).__init__(app, name, url, subdomain, index_view, translations_path, endpoint,
                                       static_url_path, base_template, 'bootstrap3', category_icon_classes)
        self.short_name = short_name or name
        self.long_name = long_name or name
        self.skin = skin

    def gravatar_image_url(self, email, default_url, size = 96):
        return "https://www.gravatar.com/avatar/" \
               + hashlib.md5(email.lower()).hexdigest() \
               + "?" + urllib.urlencode({'d': default_url, 's': str(size)})

    def set_category_icon(self, name, icon_type, icon_value):
        cat_text = as_unicode(name)
        category = self._menu_categories.get(cat_text)

        if category is not None:
            category.icon_type = icon_type
            category.icon_value = icon_value
