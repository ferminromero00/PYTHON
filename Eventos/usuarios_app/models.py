from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_app_user_set',
        related_query_name='usuario',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_app_user_set',
        related_query_name='usuario',
        blank=True
    )