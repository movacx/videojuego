from django.db import models

from jugadores.models import Jugador


class Torneo(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('abierto', 'Abierto'),
        ('en_curso', 'En curso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    nombre = models.CharField(max_length=200)
    videojuego = models.ForeignKey(
        'videojuegos.Videojuego',
        on_delete=models.CASCADE,
        related_name='torneos'
    )
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    cupo_maximo = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    premio = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVA', 'Activa'),
        ('RETIRADA', 'Retirada'),
        ('DESCALIFICADA', 'Descalificada'),
    ]

    torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    jugador = models.ForeignKey(
        Jugador,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ACTIVA')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['torneo', 'jugador'],
                name='inscripcion_unica_torneo_jugador'
            )
        ]

    def __str__(self):
        return f'{self.jugador} - {self.torneo}'