from django.db import models

from .endereco import Endereco

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    funcao = models.CharField(max_length=100)
    dataNasc = models.DateField()
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.nome}  "