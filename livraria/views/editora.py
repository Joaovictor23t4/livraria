from rest_framework.viewsets import ModelViewSet

from ..models.editora import Editora
from ..serializers.editora import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer