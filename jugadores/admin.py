from django.contrib import admin
from .models import Jugador

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'nombre', 'pais', 'nivel', 'estado')
    list_filter = ('pais', 'estado')
    search_fields = ('nickname', 'nombre', 'correo')

# Register your models here.
