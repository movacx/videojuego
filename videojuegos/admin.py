from django.contrib import admin
from .models import videojuego

@admin.register(videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'plataforma', 'estado')
    list_filter = ('plataforma', 'estado')
    search_fields = ('nombre',)
# Register your models here.
