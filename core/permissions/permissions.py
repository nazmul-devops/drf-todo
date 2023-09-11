from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

class IsProjectManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.project_manager == request.user.id:
            return True
        return False