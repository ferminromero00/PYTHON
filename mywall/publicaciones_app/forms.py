from django import forms
from .models import Publicacion, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe algo...'})
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
