from .abc import BaseModelView


class MessageView(BaseModelView):
    column_editable_list = ['from_user', 'to_user', 'subject', 'content', 'created_at']
    column_searchable_list = ['from_user.first_name', 'from_user.last_name', 'from_user.email', 'to_user.first_name',
                              'to_user.last_name', 'to_user.email', 'subject', 'content', 'created_at']
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
