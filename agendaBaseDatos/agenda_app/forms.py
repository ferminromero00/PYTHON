from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
 
        fields = ['descripcion', 'fecha']
        widget = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        } 