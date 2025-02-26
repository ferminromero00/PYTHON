from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from alojamientos_app.models import Alojamiento

@login_required
def alojamientos(request):
    return render(request, 'alojamientos.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def mis_alojamientos(request):
    alojamientos = Alojamiento.objects.filter(propietario = request.user)
    return render(request, 'mis_alojamientos.html', {'alojamientos': alojamientos})
