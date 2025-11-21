from rest_framework.viewsets import ModelViewSet

from core.models import Artefatos
from core.serializers import ArtefatosSerializer


class ArtefatosViewSet(ModelViewSet):
    queryset = Artefatos.objects.all()
    serializer_class = ArtefatosSerializer