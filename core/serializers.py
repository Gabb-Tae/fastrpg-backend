from rest_framework.serializers import ModelSerializer

from core.models import rpgclass, rpgrace, skills, itens, character
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

class characterSerializer(ModelSerializer):
    class Meta:
        model = character
        fields = "__all__"
        img_attachment_key = SlugRelatedField(
        source="img",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    img = ImageSerializer(required=False, read_only=True)


