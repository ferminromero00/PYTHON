from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model
from usuarios_app import Usuario

class RegistroForm(UserCreationForm):
    class Meta():
        model: Usuario
        fields = ['username', 'password', 'nombre_apellidos']
        