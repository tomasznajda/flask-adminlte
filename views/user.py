from .abc import BaseModelView


class UserView(BaseModelView):
    column_editable_list = ['email', 'first_name', 'last_name']
    column_searchable_list = ['email', 'first_name', 'last_name']
    column_exclude_list = ['password']
    column_details_exclude_list = ['password']
    column_filters = ['email', 'first_name', 'last_name']
    can_export = True
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = True
