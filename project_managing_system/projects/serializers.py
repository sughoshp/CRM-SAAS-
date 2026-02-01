from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "company",
            "created_by",
            "start_date",
            "end_date",
            "created_at",
        )
    
    def validate(self, data):
        user = self.context["request"].user

        # 🔒 Project must belong to same company
        project = data.get("project")
        if project and project.company != user.company:
            raise serializers.ValidationError("Project does not belong to your company")

        # 🔒 Assigned user must belong to same company
        assigned_to = data.get("assigned_to")
        if assigned_to and assigned_to.company != user.company:
            raise serializers.ValidationError("Cannot assign task to another company user")

        # Dept head rule
        if user.role == "DEPT_HEAD":
            if set(data.keys()) - {"status"}:
                raise serializers.ValidationError(
                    "You can only update task status."
                )

        return data

