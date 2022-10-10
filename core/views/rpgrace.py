from rest_framework.viewsets import ModelViewSet
from core.models import rpgrace
from core.serializers import rpgrace

class rpgraceViewSet(ModelViewSet):
    queryset = rpgrace.objects.all()
    serializer_class = rpgrace
