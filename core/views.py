from rest_framework.viewsets import ModelViewSet

from core.models import rpgclass, rpgrace, skills, itens, itensclass
from core.serializers import rpgclassSerializer, rpgraceSerializer, skillsSerializer, itensSerializer, itensclassSerializer

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

class itensclassViewSet(ModelViewSet):
    queryset = itensclass.objects.all()
    serializer_class = itensclassSerializer