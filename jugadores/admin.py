from django.contrib import admin

from jugadores.models import Jugador

# Register your models here.
@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'nombre', 'pais', 'nivel', 'estado')
    list_filter = ('pais', 'estado')
    search_fields = ('nickname', 'nombre', 'correo')