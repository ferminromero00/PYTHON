from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def alojamientos(request):
    return render(request, 'alojamientos.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')