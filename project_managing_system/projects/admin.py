# projects/admin.py
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "created_by", "created_at")
    search_fields = ("name",)
    list_filter = ("company",)
    filter_horizontal = ("members",)
    readonly_fields = ("created_at",)
