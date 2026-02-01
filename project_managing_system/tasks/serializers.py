from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_me = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "project",
            "assigned_to",
            "status",
            "start_date",
            "end_date",
            "created_at",
            "assigned_to_me",
            "company",
            "can_edit",
        )
        read_only_fields = (
            "created_at",
            "company",
        )

    def get_assigned_to_me(self, obj):
        user = self.context["request"].user
        return obj.assigned_to == user

    def get_can_edit(self, obj):
        user = self.context["request"].user

        if user.role == "ADMIN":
            return True

        if user.role == "DEPT_HEAD":
            return obj.assigned_to == user

        return False

    def validate(self, data):
        user = self.context["request"].user

        if user.role == "DEPT_HEAD":
            if set(data.keys()) - {"status"}:
                raise serializers.ValidationError(
                    "You can only update task status."
                )

        return data
