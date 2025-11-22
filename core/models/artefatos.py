from django.db import models
from core.models import categorias
from uploader.models import Image

from .localizacao import Localizacao
from .categorias import Categorias


class Artefatos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    datado = models.DateField()
    dataEntrada = models.DateField(auto_now_add=True)
    materiaPrima = models.CharField(max_length=100)
    SubMatPrima = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='artefatos/', null=True, blank=True, default=None)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, null=True, blank=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)
    peso = models.CharField(max_length=50, null=True, blank=True)
    dimensoes = models.CharField(max_length=100, null=True, blank=True)
    sitio = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    grupo_etnico = models.CharField(max_length=100, null=True, blank=True)
    sala = models.CharField(max_length=50, null=True, blank=True)
    estante = models.CharField(max_length=50, null=True, blank=True)
    prateleira = models.CharField(max_length=50, null=True, blank=True)
    observacoes_gerais = models.TextField(null=True, blank=True)
    responsavel = models.CharField(max_length=100, null=True, blank=True)
    colecao = models.CharField(max_length=100, null=True, blank=True)
    categoria_nome = models.CharField(max_length=100, null=True, blank=True)
    subtipo = models.CharField(max_length=100, null=True, blank=True)
    nivel_conservacao = models.CharField(max_length=50, null=True, blank=True)
    integridade = models.CharField(max_length=50, null=True, blank=True)
    detalhe_conservacao = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"({self.id}) {self.nome} "