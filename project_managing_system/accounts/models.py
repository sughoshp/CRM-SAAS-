from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("DEPT_HEAD", "Department Head"),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="DEPT_HEAD",
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,   # allow superuser creation
        blank=True
    )

   