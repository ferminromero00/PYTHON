from django import forms

class Formulario(forms.Form):
    descripcion = forms.CharField(required=False)
    fecha = forms.DateField(required=False, input_formats=['%d-%m-%Y'])