from django.shortcuts import render, redirect
from eventos_app.models import Evento
from eventos_app.forms import EventoForm

# Create your views here.
def index (request):
    eventos = Evento.objects.filter(usuario = request.user)
    return render(request, 'index.html', {'eventos': eventos})

def crear_evento (request):
    if(request.method == "POST"):
        form = EventoForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = EventoForm()
        
    return render(request, 'nuevoevento.html', {'form': form})