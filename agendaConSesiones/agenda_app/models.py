from django.db import models

class Cita(models.Model):
    description = models.CharField(max_length=255)
    fecha = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.fecha:
            return f"{self.description} - {self.fecha.strftime('%d-%m-%Y')}"
        else:
            return self.description