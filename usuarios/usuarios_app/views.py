from django.shortcuts import render
from usuarios_app.forms import RegistroForm

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


def inicio(request):
    return render(request, 'index.html')