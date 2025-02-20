from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Evento
from .forms import EventoForm

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario_creador = request.user
            evento.save()
            return redirect('index')
    else:
        form = EventoForm()
    return render(request, 'eventos_app/nuevoevento.html', {'form': form})

@login_required
def index(request):
    eventos = Evento.objects.filter(usuario_creador=request.user)
    return render(request, 'eventos_app/index.html', {'eventos': eventos})

@login_required
def cambiar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, usuario_creador=request.user)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos_app/nuevoevento.html', {'form': form})

@login_required
def borrar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, usuario_creador=request.user)
    if request.method == 'POST':
        evento.delete()
        return redirect('index')
    return render(request, 'eventos_app/borrar_evento.html', {'evento': evento})

@login_required
def invitar(request, evento_id):
    # Lógica para invitar a otros usuarios a un evento
    pass

@login_required
def invitados(request, evento_id):
    # Lógica para gestionar las invitaciones a un evento
    pass

@login_required
def borrar_invitacion(request, invitacion_id):
    # Lógica para eliminar una invitación
    pass

@login_required
def mis_invitaciones(request):
    # Lógica para ver los eventos a los que el usuario ha sido invitado
    pass