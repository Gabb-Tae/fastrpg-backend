from rest_framework.serializers import ModelSerializer

from core.models import rpgclass, rpgrace, skills, itens, itensclass

class rpgclassSerializer(ModelSerializer):
    class Meta:
        model = rpgclass
        fields = "__all__"

class rpgraceSerializer(ModelSerializer):
    class Meta:
        model = rpgrace
        fields = "__all__"

class skillsSerializer(ModelSerializer):
    class Meta:
        model = skills
        fields = "__all__"

class itensSerializer(ModelSerializer):
    class Meta:
        model = itens
        fields = "__all__"

class itensclassSerializer(ModelSerializer):
    class Meta:
        model = itensclass
        fields = "__all__"



