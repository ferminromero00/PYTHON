from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def alojamientos(request):
    return render(request, 'alojamientos.html')
