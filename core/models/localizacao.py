from django.db import models


class Localizacao(models.Model):
    data = models.DateField()
    CEP = models.CharField(max_length=10)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    predio = models.CharField(max_length=100)
    sala = models.CharField(max_length=50)
    prateleira = models.CharField(max_length=50)
    sitio = models.CharField(max_length=100, null=True, blank=True)
    bloco = models.CharField(max_length=100, null=True, blank=True)
    data_saida = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"({self.id} {self.sala}  "