from rest_framework.viewsets import ModelViewSet

from core.models import rpgclass, rpgrace, skills, itens
from core.serializers import rpgclassSerializer, rpgraceSerializer, skillsSerializer, itensSerializer

class rpgraceViewSet(ModelViewSet):
    queryset = rpgrace.objects.all()
    serializer_class = rpgraceSerializer

class rpgclassViewSet(ModelViewSet):
    queryset = rpgclass.objects.all()
    serializer_class = rpgclassSerializer

class skillsViewSet(ModelViewSet):
    queryset = skills.objects.all()
    serializer_class = skillsSerializer

class itensViewSet(ModelViewSet):
    queryset = itens.objects.all()
    serializer_class = itensSerializer