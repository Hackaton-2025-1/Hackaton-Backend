from rest_framework.serializers import ModelSerializer
from core.models import Funcionarios


class FuncionariosSerializer(ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'
