from rest_framework.permissions import BasePermission, SAFE_METHODS

class CanEditTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        # Read is allowed if task is visible
        if request.method in SAFE_METHODS:
            return True

        # ADMIN can edit everything
        if user.role == "ADMIN":
            return True

        # DEPT_HEAD can edit ONLY tasks assigned to them
        if user.role == "DEPT_HEAD":
            return obj.assigned_to == user

        return False
