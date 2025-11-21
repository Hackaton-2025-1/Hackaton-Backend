from rest_framework.serializers import ModelSerializer
from core.models import Categorias

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
