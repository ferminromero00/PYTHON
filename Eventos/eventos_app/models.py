from django.db import models
from usuarios_app.models import Usuario
# Create your models here.
class Evento(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	fecha = models.DateField()
	usuario = models.ForeignKey(Usuario)