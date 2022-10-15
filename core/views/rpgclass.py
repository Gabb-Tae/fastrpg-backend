from rest_framework.viewsets import ModelViewSet

from core.models import rpgclass
from core.serializers import rpgclass


class rpgclassViewSet(ModelViewSet):
    queryset = rpgclass.objects.all()
    serializer_class = rpgclass
