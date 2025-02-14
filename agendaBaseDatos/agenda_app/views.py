from django.shortcuts import render, get_object_or_404, redirect
from .forms import CitaForm
from .models import Cita

# Create your views here.

def index(request):
    
    # Si hemos recibido el formulario
    if request.method == 'POST':
        # Recogemos los datos del formulario
        form = CitaForm(request.POST)
        # Si el formulario supera la validación
        if form.is_valid():
            # grabamos los datos del formulario en la base de datos
            form.save()

    else: 
        form = CitaForm()

    # Leemos todas las citas de la base de datos
    citas = Cita.objects.all
    return render(request, "index.html", { 'form':form, 'citas': citas })

def cambiarcita(request, pk):
    # Leemos la cita de la base de datos
    cita = get_object_or_404(Cita, pk=pk)
    
    # Si cambiamos el objeto
    if request.method == "POST":
        # Recogemos el objeto que queremos actualizar
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            # Actualizamos el objeto
            if "guardar" in request:
                # Crea o actualiza
                form.save()
            else:
                # Borra  la cita
                cita.delete()
            # Y volvemos a index donde se nos mostrará el formulario y todas las citas
            return redirect('index')  
    else:
        # La prime avez muestra los datos de la cita en el formulario
        form = CitaForm(instance=cita)

    # Y en el mismo index aparece la cita para ser actualizada
    # return render(request, 'index.html', {'form': form})
    return render(request, 'editarcita.html', {'form': form})

def eliminarcita(request, pk):

    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('index')
    else:
        return render(request, 'confirmar.html', {'cita': cita})
