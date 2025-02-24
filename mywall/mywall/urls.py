"""mywall URL Configuration

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
from django.urls import path
from usuarios_app.views import registro, iniciar_sesion, cerrar_sesion, home
from publicaciones_app.views import borrar_publicacion, muro_usuario, comentar_publicacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('', home, name='home'),
    path('borrar/<int:id>/', borrar_publicacion, name='borrar_publicacion'),
    path('muro/<str:username>/', muro_usuario, name='muro_usuario'),
    path('comentar/<int:publicacion_id>/', comentar_publicacion, name='comentar_publicacion'),
]






