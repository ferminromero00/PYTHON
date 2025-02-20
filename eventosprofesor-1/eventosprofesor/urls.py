from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('eventos_app.urls')),
    path('usuarios/', include('usuarios_app.urls')),
]