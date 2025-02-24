from django.contrib import admin

# Register your models here.

from usuarios_app.models import Usuario
admin.site.register(Usuario)