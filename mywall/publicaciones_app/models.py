from django.db import models
from usuarios_app.models import Usuario

# Create your models here.

class Publicacion(models.Model):

    # Las propiedades que consideres
    contenido = models.CharField(max_length=1024)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="autor_publicacion")
    fecha = models.DateField(auto_now_add=True)
    # IMPORTANTE: Para crear la tabla intermedia a partir de un modelo, 
    # necesario cuando esa tabla tiene más atributos,
    # se utiliza la clausula through
    comentarios = models.ManyToManyField(Usuario, through="Comentario")
    imagen = models.ImageField(upload_to='publicaciones/', null=True, blank=True)
    video = models.FileField(upload_to='publicaciones/videos/', null=True, blank=True)
    # Más las propiedades que consideres
    

class Comentario(models.Model):

    contacto = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="autor_comentario")
    publicacion = models.ForeignKey(Publicacion, on_delete=models.SET_NULL, null=True, blank=True, related_name="publicacion")
    texto = models.CharField(max_length=1024)
    fecha = fecha = models.DateField(auto_now_add=True)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respuestas')



    
