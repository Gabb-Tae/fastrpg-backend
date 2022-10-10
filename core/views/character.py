from rest_framework.viewsets import ModelViewSet
from core.models import character
from core.serializers import character

class characterViewSet(ModelViewSet):
    queryset = character.objects.all()
    serializer_class = character