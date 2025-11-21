from rest_framework.serializers import ModelSerializer
from core.models import Artefatos

class ArtefatosSerializer(ModelSerializer):
    class Meta:
        model = Artefatos
        fields = '__all__'
