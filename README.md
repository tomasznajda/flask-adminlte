# Flask AdminLTE
Bootstrap [AdminLTE](https://adminlte.io/) template adapted to the flask framework using [flask-admin 1.5.2](https://flask-admin.readthedocs.io/en/latest/) and [flask-security 3.0.0](https://pythonhosted.org/Flask-Security/).\
It helps to develop pretty, easy to use admin panel for backend written in flask. 

### Live preview
http://adminlte.najdaapps.com/admin/ \
**login:** admin@admin.com \
**password:** admin

### Features
- Accounts
    - login page
    - register page
    - reset password page
    - change password page
    - gravatar profile images support
- Model Views
    - create/show/edit/delete single record
    - show list of items
    - delete selected list of items
    - export all of records to *.csv file
    - filters
    - search
    - live edit
    - crud inside modal or single page 
- Menu
    - categories
    - model views
    - links
    
### Usage
Copy directories `adminlte`, `static`, `templates` to your project.

#### Basic configuration
```python
from flask import Flask, url_for
from flask_security import Security
from flask_admin import helpers as admin_helpers
from adminlte.admin import AdminLte, admins_store

app = Flask(__name__)

security = Security(app, admins_store)
admin = AdminLte(app, skin = 'green', name = 'FlaskCMS', short_name = "<b>F</b>C", long_name = "<b>Flask</b>CMS")

@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        h = admin_helpers,
        get_url = url_for
    )
```

#### Add view for your model
```python
class DeviceView(BaseAdminView):
    column_editable_list = ['name', 'type', 'rooted']
    column_searchable_list = ['name', 'type', 'rooted']
    column_exclude_list = None
    column_details_exclude_list = None
    column_filters = ['name', 'type', 'rooted']
    can_export = True
    can_view_details = False
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = False
    

admin.add_view(DeviceView(Device, db.session, name = "Devices", menu_icon_value = 'fa-laptop'))
```

#### Add link
```python
admin.add_link(FaLink(name='Website', url='http://tomasznajda.com', icon_value = 'fa-globe', target = "_blank"))
```

#### Add category
```python
admin.add_view(DeviceView(Device, db.session, name = "Devices", category='Author', menu_icon_value = 'fa-laptop'))
admin.add_link(FaLink(name='Website', category='Author', url='http://tomasznajda.com', icon_value = 'fa-globe', target = "_blank"))
admin.set_category_icon(name='Author', icon_type = 'fa', icon_value = 'fa-address-card')

```

### Configuration

#### Basic AdminLTE configuration:

- `app` -> Flask application object
- `name` -> Eg. `FlaskCMS`. Application name. Will be displayed as a page title. Defaults to "Admin"
- `short_name` -> Eg. `<b>F</b>C`. Short application name. Will be displayed in the collapsed menu bar. By default will use value of the name property.
- `long_name` -> Eg. `<b>Flask</b>CMS`. Long application name. Will be displayed in the expanded menu bar and above each security form. By default will use value of the name property.
- `skin` -> AdminLTE skin color (`blue`, `black`, `puprle`, `green`, `red`, `yellow`, `blue-light`, `black-light`, `purple-light`, `green-light`, `red-light`, `yellow-light`). By default will use `blue`.
- `url` -> Base URL
- `subdomain` -> Subdomain to use
- `index_view` -> Home page view to use. Defaults to `AdminIndexView`.
- `translations_path` -> Location of the translation message catalogs. By default will use the translations shipped with Flask-Admin.
- `endpoint` -> Base endpoint name for index view. If you use multiple instances of the `Admin` class with a single Flask application, you have to set a unique endpoint name for each instance.
- `static_url_path` -> Static URL Path. If provided, this specifies the default path to the static url directory for all its views. Can be overridden in view configuration.
- `base_template` -> Override base HTML template for all static views. Defaults to `admin/base.html`.


#### ModelViews configuration:
- list of columns that can be edited
```python
column_editable_list = ['from_user', 'to_user', 'subject', 'content', 'created_at']
```
- list of columns that should be taken into account during search, if None - search field will be hidden
```python
column_searchable_list = ['from_user.first_name', 'from_user.last_name', 'from_user.email', 'to_user.first_name',
                          'to_user.last_name', 'to_user.email', 'subject', 'content', 'created_at']
```
- list of columns that should be omitted on the list page,  if None - all columns will be shown
```python
column_exclude_list = ['created_at']
```
- list of columns that should be omitted on the details page or modal, if None - all columns will be shown
```python
column_details_exclude_list = ['created_at']
```
- list of columns that can be used as filters, if None - filters button will be hidden.
```python
column_filters = ['subject', 'content', 'created_at']
```
- enabling features
```python
can_export = True
can_view_details = True
can_create = True
can_edit = True
can_delete = True
```
- modal or page
```python
edit_modal = True
create_modal = True
details_modal = True
```

#### Security configuration:
- enable register form
```python
SECURITY_REGISTERABLE = True
```
- enable forgot password form
```python
SECURITY_RECOVERABLE = True
```
- enable change password form
```python
SECURITY_CHANGEABLE = True
```

