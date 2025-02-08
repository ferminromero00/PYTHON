from django.shortcuts import render
from .forms import MiFormulario

def formulario_vista(request):
    nombre = ""

    if request.method == "POST":
        form = MiFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]  
    else:
        form = MiFormulario()

    return render(request, "formulario.html", {"form": form, "nombre": nombre})