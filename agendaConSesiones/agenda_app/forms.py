from django import forms

class Formulario(forms.Form):
    descripcion = forms.CharField(required=False)
    fecha = forms.DateField(required=False)