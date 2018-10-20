from .abc import BaseModelView


class RoleView(BaseModelView):
    column_editable_list = None
    column_searchable_list = None
    column_exclude_list = None
    column_details_exclude_list = None
    column_filters = None
    can_export = False
    can_view_details = False
    can_create = False
    can_edit = False
    can_delete = False
    edit_modal = False
    create_modal = False
    details_modal = False
