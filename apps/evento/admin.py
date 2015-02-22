from django.contrib import admin
from .models import Evento, Categoria, Asistente, Comentario
# Register your models here.

admin.site.register(Evento)
admin.site.register(Categoria)
admin.site.register(Asistente)
admin.site.register(Comentario)
