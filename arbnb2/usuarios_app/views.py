from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from alojamientos_app.models import Alojamiento, Alquiler
from alojamientos_app.forms import AlojamientoForm, AlquilerForm

@login_required
def alojamientos(request):
    return render(request, 'alojamientos.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def mis_alojamientos(request):
    alojamientos = Alojamiento.objects.filter(propietario=request.user)
    return render(request, 'alojamientos.html', {'alojamientos': alojamientos})


def ver_alquileres(request, id):
    alquileres = Alquiler.objects.filter(alojamiento_id=id)
    return render(request, 'ver_alquileres.html', {'alquileres': alquileres})
