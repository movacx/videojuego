from rest_framework import serializers
from .models import videojuego

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videojuego
        fields = '__all__'
        