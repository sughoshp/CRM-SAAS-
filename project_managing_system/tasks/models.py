from django.db import models
from projects.models import Project
from django.conf import settings
from companies.models import Company

class Task(models.Model):
    STATUS_CHOICES = (
        ("IN_PROG", "IN PROGRESS"),
        ("DONE", "COMPLETED"),
        ("TODO", "ASSIGNED"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_tasks"
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_tasks"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="TODO"
    )

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.project.name})"
