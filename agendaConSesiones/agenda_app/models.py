from django.db import models

# Create your models here.
class Cita():
    def __init__(self, description, fecha):
        self.description=description
        self.fecha=fecha