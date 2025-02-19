from django.shortcuts import render
from eventos_app.models import Evento

# Create your views here.
def index (request):
    eventos = Evento.objects.all
    return render(request, 'index.html', {'eventos': eventos})