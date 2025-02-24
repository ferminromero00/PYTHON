from django.urls import path
from .views import registro, iniciar_sesion, cerrar_sesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
