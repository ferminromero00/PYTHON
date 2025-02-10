from django.shortcuts import render
from agenda_app.forms import Formulario;
from agenda_app.models import Cita

# Create your views here.
def index(request):
    if "agenda" not in request.session:
        request.session["agenda"] = []
    
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            descripcion = form.cleaned_data["descripcion"]
            fecha = form.cleaned_data["fecha"]
            cita = Cita(descripcion, fecha)
            request.session["agenda"].append(cita)
        else:
            form = Formulario()
        
        return render(request, 'index.html', {'form':form, 'agenda': request.session["agenda"]})