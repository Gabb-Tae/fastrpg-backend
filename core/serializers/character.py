from rest_framework.serializers import ModelSerializer
from core.models import character
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from media.models import Image
from media.serializers import ImageSerializer

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


