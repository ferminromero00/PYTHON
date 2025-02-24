from django.contrib import admin


from .models import Publicacion
from .models import Comentario


admin.site.register(Publicacion)
admin.site.register(Comentario)