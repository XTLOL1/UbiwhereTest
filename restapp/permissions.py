from rest_framework import permissions

class IsAdminOrAnonReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff is True:
                return True
        return False
