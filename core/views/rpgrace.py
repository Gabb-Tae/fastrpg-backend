from rest_framework.viewsets import ModelViewSet

from core.models import rpgrace
from core.serializers import rpgraceSerializer


class rpgraceViewSet(ModelViewSet):
    queryset = rpgrace.objects.all()
    serializer_class = rpgraceSerializer
