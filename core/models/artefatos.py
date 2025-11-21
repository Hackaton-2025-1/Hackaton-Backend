from django.db import models

class Artefatos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    datado = models.DateField()
    dataEntrada = models.DateField(auto_now_add=True)
    materiaPrima = models.CharField(max_length=100)
    SubMatPrima = models.CharField(max_length=100)
    # localizacao = models.ForeignKey('localizacao')
    # img = models.ForeignKey('Imagens', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.nome} "