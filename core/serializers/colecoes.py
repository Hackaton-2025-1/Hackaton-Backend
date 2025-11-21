from rest_framework.serializers import ModelSerializer
from core.models import Colecoes


class ColecoesSerializer(ModelSerializer):
    class Meta:
        model = Colecoes
        fields = '__all__'
