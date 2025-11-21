from django.db import models

class Colecoes(models.Model):
    nome = models.CharField(max_length=100)
    PeriodoData = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"({self.id}) {self.nome}  "