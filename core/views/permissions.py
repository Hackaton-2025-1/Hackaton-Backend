from .permissions import IsAdminOrReadOnly
from .Artefatos import ArtefatosSerializer

class ArtefatoViewSet(viewsets.ModelViewSet):
    queryset = Artefatos.objects.all()
    serializer_class = ArtefatosSerializer
    permission_classes = [IsAdminOrReadOnly]