from django.db import models
from datetime import datetime


class BaseUserModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Investimento(BaseUserModel):
    investimento = models.CharField(max_length=100)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
