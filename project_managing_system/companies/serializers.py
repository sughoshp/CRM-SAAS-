from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "description",
            "created_by",
            "created_at",
            "updated_at",
        )
