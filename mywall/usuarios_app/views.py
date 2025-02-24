from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from publicaciones_app.models import Publicacion
from publicaciones_app.forms import PublicacionForm
from .models import Publicacion


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('home')  
    else:
        form = PublicacionForm()

    publicaciones = Publicacion.objects.filter(autor=request.user).order_by('-fecha')
    return render(request, 'home.html', {'form': form, 'publicaciones': publicaciones})

def borrar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('home')
    return render(request, 'confirmar_borrado.html', {'publicacion': publicacion})