from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required


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
    return render(request, 'home.html')