from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect("mis_alojamientos")

    if (request.method == "POST"):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("mis_alojamientos")
        else:
            form = AuthenticationForm()
            return render(request, "login.html", {'form': form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect("login")