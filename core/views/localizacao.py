from rest_framework.viewsets import ModelViewSet

from core.models import Localizacao
from core.serializers import LocalizacaoSerializer


class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
