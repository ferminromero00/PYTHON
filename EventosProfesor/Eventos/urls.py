"""Eventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from eventos_app.views import index, crear_evento, cambiar_evento, borrar_evento, invitados, invitar, borrar_invitacion, mis_invitaciones
from usuarios_app.views import salir

    
urlpatterns = [
    
    # path('eventos/', include('usuarios_app/urls')),
    path('evento/nuevo/', crear_evento, name='crear_evento'),
    path('evento/editar/<int:pk>/', cambiar_evento, name='cambiar_evento'),
    path('evento/borrar/<int:pk>/', borrar_evento, name='borrar_evento'),
    path('evento/invitados/<int:pk>/', invitados, name='invitados'),
    path('evento/invitar/<int:pkusuario>/<int:pkevento>/', invitar, name='invitar'),
    path('evento/borrarinvitacion/<int:pkusuario>/<int:pkevento>/', borrar_invitacion, name='borrar_invitacion'),
    path('misinvitaciones', mis_invitaciones, name='mis_invitaciones'),
    path('salir/', salir, name='salir'),
    path('index/', index, name="index"),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
]
