from rest_framework import serializers
from .models import Torneo, videojuego

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'

    def validate_cupo_maximo(self, value):
        if value <= 2:
            raise serializers.ValidationError("El cupo máximo debe ser mayor a dos.")
        return value 

    def validate(self, data):
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        videojuego = data.get('videojuego')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        if videojuego and not videojuego.activo:
            raise serializers.ValidationError("El videojuego no está disponible para torneos.")
        return data