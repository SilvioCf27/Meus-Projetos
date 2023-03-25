# Criar os modelos aqui.

from django.db import models

class TipoDoce(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Doce(models.Model):
    tipo = models.ForeignKey(TipoDoce, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)