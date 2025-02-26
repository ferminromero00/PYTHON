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
# urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from usuarios_app import views
from usuarios_app.views import mis_alojamientos
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('alojamientos/', views.mis_alojamientos, name='alojamientos'),
    path('editar_alojamiento/<int:id>/', views.editar_alojamiento, name='editar_alojamiento'),
    path('ver_alquileres/<int:id>/', views.ver_alquileres, name='ver_alquileres'),
    path('crear_alojamiento', views.crear_alojamiento, name='crear_alojamiento'),
    path('alquilar', views.alquilar, name='alquilar'),
]

