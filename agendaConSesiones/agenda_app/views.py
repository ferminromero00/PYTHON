from django.shortcuts import render
from agenda_app.forms import Formulario
from agenda_app.models import Cita

def index(request):
    if "agenda" not in request.session:
        request.session["agenda"] = []

    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            descripcion = form.cleaned_data["descripcion"]
            fecha = form.cleaned_data["fecha"]

            # Guardar la cita en formato de diccionario (serializable)
            cita = {
                "descripcion": descripcion,
                "fecha": fecha.strftime("%d-%m-%Y") if fecha else None 
            }

            request.session["agenda"].append(cita)
            request.session.modified = True

    else:
        form = Formulario()

    return render(request, 'index.html', {'form': form, 'agenda': request.session["agenda"]})
