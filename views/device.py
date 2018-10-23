from adminlte.views import BaseAdminView


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
