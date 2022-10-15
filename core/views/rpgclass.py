from rest_framework.viewsets import ModelViewSet

from core.models import rpgclass
from core.serializers import rpgclassSerializer


class rpgclassViewSet(ModelViewSet):
    queryset = rpgclass.objects.all()
    serializer_class = rpgclassSerializer