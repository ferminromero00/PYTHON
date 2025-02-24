from django import forms
from .models import Publicacion, Comentario

class PublicacionForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'accept': 'image/*',
        'class': 'form-control'
    }))
    
    class Meta:
        model = Publicacion
        fields = ['contenido', 'imagen']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe algo...'})
        }

    def save(self, commit=True):
        publicacion = super().save(commit=False)
        if commit:
            publicacion.save()
        return publicacion

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

    def save(self, commit=True):
        comentario = super().save(commit=False)
        if commit:
            comentario.save()
        return comentario

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 2, 
                'placeholder': 'Escribe una respuesta...', 
                'class': 'respuesta-textarea'
            })
        }