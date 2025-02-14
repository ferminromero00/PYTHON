from django.shortcuts import render, redirect
from .forms import CitaForm
from .models import Cita

# Create your views here.
def index(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
        else:
            form = CitaForm(request.POST)
        return render(request, "index.html", {'form': form})
    else:
        form = CitaForm()
    return render(request, "index.html", {'form': form})

def cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
            return redirect('citas')
    else:
        form = CitaForm()
    return render(request, 'cita.html', {'form': form})