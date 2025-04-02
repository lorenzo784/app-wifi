from django.db import models

class DispositivoIoT(models.Model):
    nombre = models.CharField(max_length=100, default="Dispositivo Único")
    encendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre