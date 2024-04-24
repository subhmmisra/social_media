from rest_framework import permissions
from datetime import timezone
from apps.base.exceptions import BadRequest

class IsAuthenticatedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Check if user is authenticated
        """
        return (request.user.is_authenticated and request.user.is_active)

        
