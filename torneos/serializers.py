from rest_framework import serializers
from .models import Torneo, Inscripcion

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

    def validate_cupo_maximo(self, value):
        if value <= 2:
            raise serializers.ValidationError("El cupo máximo debe ser al menos 2.")
        return value

    def validate(self, data):
        fecha_inicio=data.get('fecha_inicio')
        fecha_fin=data.get('fecha_fin')
        videojuego=data.get('videojuego')

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise serializers.ValidationError({
                "fecha_fin": "La fecha de fin debe ser posterior a la fecha de inicio."
            })
        
        if videojuego and not videojuego.activo:
            raise serializers.ValidationError({
                "videojuego": "No se puede usar un videojuego inactivo."
            })
        
        return data
    