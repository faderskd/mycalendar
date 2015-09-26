from rest_framework import permissions


class IsRequestAjax(permissions.BasePermission):
    """
    Rejects all request which are not ajax
    """

    def has_permission(self, request, view):
        return request.is_ajax()
