from django.db import models
from uploader.models import Image

class Artefatos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    datado = models.DateField()
    dataEntrada = models.DateField(auto_now_add=True)
    materiaPrima = models.CharField(max_length=100)
    SubMatPrima = models.CharField(max_length=100)
    imagem = models.ForeignKey(
        Image,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"({self.id}) {self.nome} "