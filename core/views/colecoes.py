from rest_framework.viewsets import ModelViewSet

from core.models import Colecoes
from core.serializers import ColecoesSerializer


class ColecoesViewSet(ModelViewSet):
    queryset = Colecoes.objects.all()
    serializer_class = ColecoesSerializer
