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
from usuarios_app.views import registro, iniciar_sesion, cerrar_sesion
from publicaciones_app.views import borrar_publicacion, muro_usuario, comentar_publicacion, home, responder_comentario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro, name='registro'),
    path('', iniciar_sesion, name='login'),  # Cambiado a ruta raíz
    path('logout/', cerrar_sesion, name='logout'),
    path('home/', home, name='home'),  # Movido home a /home/
    path('borrar/<int:id>/', borrar_publicacion, name='borrar_publicacion'),
    path('muro/<str:username>/', muro_usuario, name='muro_usuario'),
    path('comentar/<int:publicacion_id>/', comentar_publicacion, name='comentar_publicacion'),
    path('responder/<int:comentario_id>/', responder_comentario, name='responder_comentario'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






