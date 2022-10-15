from rest_framework.viewsets import ModelViewSet

from core.models import itens
from core.serializers import itensSerializer


class itensViewSet(ModelViewSet):
    queryset = itens.objects.all()
    serializer_class = itensSerializer