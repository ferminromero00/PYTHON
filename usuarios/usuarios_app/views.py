from django.shortcuts import render, redirect
from usuarios_app.forms import RegistroForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # login(request, usuario)
            return render(request, 'registro.html', {'form': form})
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def inicio(request):
    return render(request, 'index.html')

def salir(request):
    logout(request)
    return redirect('login')
