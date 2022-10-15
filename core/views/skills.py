from rest_framework.viewsets import ModelViewSet

from core.models import skills
from core.serializers import skills


class skillsViewSet(ModelViewSet):
    queryset = skills.objects.all()
    serializer_class = skills
