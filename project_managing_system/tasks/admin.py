# tasks/admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "project",
        "assigned_to",
        "status",
        "created_by",
        "created_at",
    )

    list_filter = ("status", "project")
    search_fields = ("name", "description")
    readonly_fields = ("created_at",)

    autocomplete_fields = ("project", "assigned_to", "created_by")
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
