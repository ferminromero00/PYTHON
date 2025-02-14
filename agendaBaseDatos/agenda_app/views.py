from django.shortcuts import render, get_object_or_404, redirect
from .models import Cita
from .forms import CitaForm

def index(request):
    form = CitaForm()
    return render(request, 'index.html', {'form': form})

def citas(request):
    citas = Cita.objects.all()
    return render(request, 'vercitas.html', {'citas': citas})

def cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
            return redirect('citas')
    else:
        form = CitaForm()
    return render(request, 'cita.html', {'form': form})

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    
    if request.method == "POST":
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas')  # Redirigir tras la edición
    else:
        form = CitaForm(instance=cita)

    return render(request, 'citaeditar.html', {'form': form})

def borrar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    
    if request.method == 'POST':  # Solo borra si se confirma
        cita.delete()
        return redirect('citas')

    return render(request, 'citas/cita_confirm_delete.html', {'cita': cita})