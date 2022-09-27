from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import rpgclass, rpgrace, skills, itens, character
from core.serializers import rpgclassSerializer, rpgraceSerializer, skillsSerializer, itensSerializer, characterSerializer

class rpgraceViewSet(ModelViewSet):
    queryset = rpgrace.objects.all()
    serializer_class = rpgraceSerializer
    permission_classes = [IsAuthenticated]
    
class rpgclassViewSet(ModelViewSet):
    queryset = rpgclass.objects.all()
    serializer_class = rpgclassSerializer
    permission_classes = [IsAuthenticated]

class skillsViewSet(ModelViewSet):
    queryset = skills.objects.all()
    serializer_class = skillsSerializer
    permission_classes = [IsAuthenticated]

class itensViewSet(ModelViewSet):
    queryset = itens.objects.all()
    serializer_class = itensSerializer
    permission_classes = [IsAuthenticated]

class characterViewSet(ModelViewSet):
    queryset = character.objects.all()
    serializer_class = characterSerializer
    permission_classes = [IsAuthenticated]