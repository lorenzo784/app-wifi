from django.db import models

class DispositivoIoT(models.Model):
    nombre = models.CharField(max_length=100, default="Dispositivo Único")
    encendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class DatoSensor(models.Model):
    valor = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    humedad = models.FloatField(null=True, blank=True)
    temperatura = models.FloatField(null=True, blank=True)
    distancia = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.valor} - {self.fecha}"
