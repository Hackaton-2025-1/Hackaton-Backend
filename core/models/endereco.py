from django.db import models

class Endereco(models.Model):
    CEP = models.CharField(max_length=10)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    

    def __str__(self):
        return f"({self.CEP}  "