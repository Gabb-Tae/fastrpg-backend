from rest_framework.viewsets import ModelViewSet

from core.models import zcharacter


class zcharacterViewSet(ModelViewSet):
    queryset = zcharacter.objects.all()
    serializer_class = zcharacter