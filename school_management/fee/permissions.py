from rest_framework.permissions import BasePermission

class IsAdminOrOfficeStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.is_officestaff
        )
