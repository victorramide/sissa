from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Advogado(models.Model):
    user = models.OneToOneField(
        User, related_name='advogado', on_delete=models.CASCADE)
    oab = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.oab}/{self.uf}'
