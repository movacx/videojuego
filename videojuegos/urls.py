from django.urls import path
from . import views

urlpatterns = [
    path('', views.videojuegos_api, name='videojuegos_api'),
]