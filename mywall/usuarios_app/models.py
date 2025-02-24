from django.db import models
from django.contrib.auth.models import AbstractUser 


# Create your models here.

class Usuario(AbstractUser):

    # Las propiedades que consideres
    telefono = models.CharField(max_length=15)

    