from rest_framework.viewsets import ModelViewSet

from core.models import zcharacter
from core.serializers import characterSerializer
from core.serializers.zcharacter import characterSerializer


class characterViewSet(ModelViewSet):
    queryset = zcharacter.objects.all()
    serializer_class = characterSerializer