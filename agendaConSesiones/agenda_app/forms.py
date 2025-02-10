from django.db import forms

class Formulario(forms.Form):
    descripcion=forms.textField()
    fecha = forms.DateField()