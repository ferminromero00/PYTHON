from django.shortcuts import render
from usuarios_app.forms import RegistroForm

# Create your views here.
def registro(request):
 if request.method == 'POST':
   form = RegistroForm(request.POST)
   if form.isValid():
       usuario = form.save()
       #login(request, usuario)
   else:
       form = RegistroForm()
   return render(request, 'registro.html', {'form': form})    