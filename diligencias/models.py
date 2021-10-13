from datetime import datetime

from django.db import models

from advogados.models import Advogado


class Diligencia(models.Model):
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    processo = models.CharField(max_length=30)
    classe = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, default='Despacho')
    diligencia = models.TextField()
    prioridade = models.BooleanField(default=False)
    data_diligencia = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.processo
