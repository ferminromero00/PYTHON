from django import forms

class CitaForm(forms.Form):
    descripcion = forms.CharField(required=False)
    fecha = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))