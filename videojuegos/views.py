from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import videojuego
from .serializers import VideojuegoSerializer

@api_view(['GET', 'POST'])

def videojuegos_api(request):
    if request.method == 'GET':
        videojuegos = videojuego.objects.filter(estado = True).order_by('nombre')
        plataforma = request.query_params.get('plataforma')

        if plataforma:
            videojuegos = videojuegos.filter(plataforma__iexact = plataforma )
    
    
        serializer = VideojuegoSerializer(videojuegos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.

    if not request.user.is_authenticated or not request.user.is_staff:
        return Response({'error': 'No tienes permiso para realizar esta acción.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = VideojuegoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
