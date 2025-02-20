from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento

        fields=['titulo', 'descripcion', 'fecha'] 
        # No mostramos el campo usuario
        exclude=['usuario']
        widget = {
            'titulo': forms.TextInput,
            'descripcion': forms.TextInput,        
            # revisar
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }