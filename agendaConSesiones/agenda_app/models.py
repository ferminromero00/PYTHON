from django.db import models

class Cita(models.Model):
    description = models.CharField(max_length=255)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.description} - {self.fecha.strftime('%d-%m-%Y')}"