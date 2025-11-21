from rest_framework.viewsets import ModelViewSet

from core.models import Funcionarios
from core.serializers import FuncionariosSerializer


class FuncionariosViewSet(ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer
