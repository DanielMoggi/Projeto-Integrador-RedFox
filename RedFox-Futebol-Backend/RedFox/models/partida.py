from django.db import models
from RedFox.models import Time

class Partida(models.Model):
    times = models.ManyToManyField(Time)
    data = models.DateTimeField()
    def __str__(self):
        return self.descricao