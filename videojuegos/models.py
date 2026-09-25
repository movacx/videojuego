from django.db import models
# Create your models here.

class videojuego(models.Model):
    nombre = models.CharField(max_length=120)
    genero = models.CharField(max_length=80)
    plataforma = models.CharField(max_length=80)
    clasificacion = models.CharField(max_length=30, blank = True)
    fecha_lanzamiento = models.DateField(null = True, blank = True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    