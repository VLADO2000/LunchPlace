from rest_framework import permissions

class IsRestauranter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1

class IsViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 0