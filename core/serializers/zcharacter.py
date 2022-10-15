from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import zcharacter
from media.models import Image
from media.serializers import ImageSerializer


class zcharacterSerializer(ModelSerializer):
    img_attachment_key = SlugRelatedField(
        source="img",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    img = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = zcharacter
        fields = "__all__"