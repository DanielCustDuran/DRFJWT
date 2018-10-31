from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.is_admin:
            return True
        elif request.method == 'GET':
            return True
        return request.user and request.user.is_admin
