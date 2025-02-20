from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from usuarios_app.models import Usuario
from .forms import EventoForm

# Create your views here.

def index(request):

    # Recoger los eventos del suaurio
    eventos = Evento.objects.filter(usuario = request.user)
    
    return render(request, 'index.html', {'eventos': eventos})

def crear_evento(request):

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # Recogemos el evento pero no lo guardamos
            evento = form.save(commit=False)
            # Le asignamos el usuario
            evento.usuario = request.user
            # Y ahora sí lo grabamos
            evento.save()
            # Mostramos de nuevo las citas
            return redirect('index')
    else:
        form = EventoForm()
    
    return render(request, 'nuevoevento.html', {'form': form})

def cambiar_evento(request, pk):

    # recogemos el evento
    evento = get_object_or_404(Evento, pk=pk)

    if request.method == 'POST':
        # se lo pasamos al formulario para que lo edite
        form = EventoForm(request.POST, instance=evento)
        # recogemos el evento actualizado
        if form.is_valid():
            # Recogemos el evento y lo guardamos porque ya tiene al usuario asociadp
            form.save()            
            return redirect('index')
    else:
        # se lo pasamos al formulario para que lo edite
        form = EventoForm(instance=evento)
    
    # mostramos el formulario de edición
    return render(request, 'nuevoevento.html', {'form': form})

def borrar_evento(request, pk):

    # recogemos el evento
    evento = get_object_or_404(Evento, pk=pk)

    if request.method == 'POST':
        # borramos el evento
        evento.delete()
    
    # mostramos los eventos del usuario
    return redirect('index')

def invitados(request, pk):

    # recogemos el evento
    evento = get_object_or_404(Evento, pk=pk)
    # leemos todos los usuarios
    usuarios = Usuario.objects.all

    # mostraremos el evento con sus invitados y totos los usuarios
    return render(request, 'invitados.html', {'evento': evento, 'usuarios':usuarios})

def invitar(request, pkusuario, pkevento):

    # recogemos el usuario al que queremos invitar
    usuario = get_object_or_404(Usuario, pk=pkusuario)
    # recogemos el evento sobre el que estamos trabajando
    evento = get_object_or_404(Evento, pk=pkevento)

    # añadimos el usuario al evento
    evento.invitados.add(usuario)
    # guardamos el evento
    evento.save()
    # nos quedamos en la misma página
    return redirect('invitados', pkevento)

def borrar_invitacion(request, pkusuario, pkevento):

    # recogemos el usuario al que queremos borrar del evento
    usuario = get_object_or_404(Usuario, pk=pkusuario)
    # recogemos el evento sobre el que estamos trabajando
    evento = get_object_or_404(Evento, pk=pkevento)
    # eliminamos al usuario
    evento.invitados.remove(usuario)
    # grabamos el evento
    evento.save()
    # volvemos a la misma página
    return redirect('invitados', pkevento)


def mis_invitaciones(request):
    
    usuario = request.user  # Obtenemos el usuario autenticado
    eventos = usuario.invitaciones.all()  # Accedemos a los eventos donde hemos sido invitados a través de related_name
    return render(request, 'misinvitaciones.html', {'eventos': eventos})

    