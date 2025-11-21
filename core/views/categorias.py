from rest_framework.viewsets import ModelViewSet

from core.models import Categorias
from core.serializers import CategoriasSerializer


class CategoriasViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer