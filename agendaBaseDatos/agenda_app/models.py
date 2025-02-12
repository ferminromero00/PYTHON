from django.db import models

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField()