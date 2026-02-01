from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from companies.permissions import IsAdminUserRole ,IsDeptHeadUserRole
from project_managing_system.permissions import CanEditTask


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanEditTask]
    
    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Task.objects.select_related(
                "project", "company", "assigned_to"
            )

        if user.role == "DEPT_HEAD":
            return Task.objects.filter(
                project__members=user
            ).select_related(
                "project", "company", "assigned_to"
            )
        return Task.objects.none()


    def get_permissions(self):
        # Only ADMIN can create or delete
        if self.action in ["create", "destroy"]:
            return [IsAuthenticated(), IsAdminUserRole()]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            company=serializer.validated_data["project"].company
        )
