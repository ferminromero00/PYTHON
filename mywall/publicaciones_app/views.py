from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion

def borrar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('home')
