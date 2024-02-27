from django.db import models

class Estado(models.TextChoices):
    PENDIENTE = 'Pendiente'
    CONFIRMADO = 'Confirmado'
    CANCELADO = 'Cancelado'

class Local(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    coordenadas = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombres = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self):
        return f"{self.nombres} - {self.fecha} - {self.hora}"