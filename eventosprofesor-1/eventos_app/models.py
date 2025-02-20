from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_creados')
    usuarios_invitados = models.ManyToManyField(User, related_name='eventos_invitados', blank=True)

    def __str__(self):
        return self.titulo

class Usuario(User):
    # Aquí puedes agregar campos adicionales si es necesario
    pass