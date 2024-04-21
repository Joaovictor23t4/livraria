from rest_framework.viewsets import ModelViewSet

from ..models.autor import Autor
from ..serializers.autor import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer