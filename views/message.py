from adminlte.views import BaseAdminView


class MessageView(BaseAdminView):
    column_editable_list = ['subject', 'content', 'created_at']
    column_searchable_list = ['subject', 'content', 'created_at']
    column_exclude_list = None
    column_details_exclude_list = None
    column_filters = ['subject', 'content', 'created_at']
    can_export = True
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = True
