from django.db import models
from django import forms
from usuarios_app.models import Usuario

# Create your models here.

class Evento(models.Model):

    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    # related_name se utiliza para poder nombrar las tablas sin que haya repetición ni ambiguedad
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="miseventos")
    invitados = models.ManyToManyField(Usuario, related_name="invitaciones")
    
  


