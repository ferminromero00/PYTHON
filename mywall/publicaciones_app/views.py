from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario
from .forms import PublicacionForm, ComentarioForm
from usuarios_app.models import Usuario

@login_required
def home(request):
    """Muestra el muro del usuario autenticado con sus publicaciones."""
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('home')
    else:
        form = PublicacionForm()

    publicaciones = Publicacion.objects.filter(autor=request.user).order_by('-fecha')
    comentario_form = ComentarioForm()

    return render(request, 'home.html', {
        'form': form,
        'publicaciones': publicaciones,
        'comentario_form': comentario_form
    })


@login_required
def muro_usuario(request, username):
    """Permite ver el muro de otro usuario sin publicar, pero con la opción de comentar."""
    usuario = get_object_or_404(Usuario, username=username)
    publicaciones = Publicacion.objects.filter(autor=usuario).order_by('-fecha')
    comentario_form = ComentarioForm()

    return render(request, 'muro_usuario.html', {
        'usuario': usuario,
        'publicaciones': publicaciones,
        'comentario_form': comentario_form
    })


@login_required
def comentar_publicacion(request, publicacion_id):
    """Permite a los usuarios comentar en una publicación."""
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion  # Asociar comentario con la publicación
            comentario.contacto = request.user  # Asociar comentario con el usuario
            comentario.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))



@login_required
def borrar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)

    if publicacion.autor != request.user:
        return redirect('home')  # Evita que otros borren publicaciones ajenas

    if request.method == 'POST':
        publicacion.delete()
        return redirect('home')

    return redirect('home')
