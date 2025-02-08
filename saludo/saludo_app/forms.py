from django import forms

class MiFormulario(forms.Form): nombre = forms.CharField(label="Tu nombre", max_length=100)