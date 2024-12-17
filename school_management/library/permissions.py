from rest_framework.permissions import BasePermission

class IsAdminOrLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.is_librarian
        )
