from rest_framework.serializers import ModelSerializer

from core.models import rpgclass, rpgrace, skills, itens
from rest_framework.serializers import ModelSerializer,                    SlugRelatedField

from media.models import Image
from media.serializers import ImageSerializer

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


