from django.contrib import admin
from .models import Torneo, Inscripcion


@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'videojuego', 'fecha_inicio', 'fecha_fin', 'cupo_maximo', 'estado', 'activo')
    list_filter = ('videojuego', 'estado', 'activo')
    search_fields = ('nombre', 'videojuego__nombre')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('torneo', 'jugador', 'fecha_inscripcion', 'estado')
    list_filter = ('torneo', 'estado')
    search_fields = ('torneo__nombre', 'jugador__nickname')
    

# Register your models here.
