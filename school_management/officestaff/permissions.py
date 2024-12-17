from rest_framework.permissions import BasePermission

class IsOfficeStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_officestaff
