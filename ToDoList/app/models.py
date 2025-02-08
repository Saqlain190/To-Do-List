from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Avoids conflict with default user_set
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Avoids conflict
        blank=True
    )
