from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm

# Create your views here.

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
    return redirect("login")