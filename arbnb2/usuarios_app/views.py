from django.shortcuts import render,redirect, get_object_or_404
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
    alojamiento = Alojamiento.objects.get(id=id)
    return render(request, 'ver_alquileres.html', {'alquileres': alquileres, 'alojamiento': alojamiento})

def editar_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, id=id, propietario=request.user)
    
    if request.method == 'POST':
        form = AlojamientoForm(request.POST, instance=alojamiento)
        if form.is_valid():
            form.save()
            return redirect('alojamientos')
    else:
        form = AlojamientoForm(instance=alojamiento)
    
    return render(request, 'editar_alojamiento.html', {'form': form, 'alojamiento': alojamiento})