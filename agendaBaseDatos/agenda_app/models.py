from django.db import models

# Create your models here.
class Cita(models.Model):
    #fecha = models.DateField(auto_now_add=True)
    fecha = models.DateField(max_length=100)
    descripcion = models.CharField()