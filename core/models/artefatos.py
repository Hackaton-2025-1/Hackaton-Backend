from django.db import models
from uploader.models import Image

from .localizacao import Localizacao


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

    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"({self.id}) {self.nome} "