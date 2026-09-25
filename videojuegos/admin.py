from django.contrib import admin
from .models import Videojuego

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'plataforma', 'estado')
    list_filter = ('plataforma', 'estado')
    search_fields = ('nombre',)

