from django.db import models
from django.conf import settings
from companies.models import Company


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_projects"
    )

    # this is just for people who are going to be part of this project and will have permission to List details 
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="members_projects")


    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.company.name})"
