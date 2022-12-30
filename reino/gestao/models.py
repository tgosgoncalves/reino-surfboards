from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class Orcamento(models.Model):
    cliente = models.CharField(max_length=150)
    orcamento_id = models.AutoField(primary_key = True)
    servico = models.CharField(max_length=150)
    material = models.CharField(max_length=150)
    quantidade = models.IntegerField()
    valor_do_orcamento = models.FloatField()

