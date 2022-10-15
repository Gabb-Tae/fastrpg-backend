from rest_framework.serializers import ModelSerializer

from core.models import rpgclass


class rpgclassSerializer(ModelSerializer):
    class Meta:
        model = rpgclass
        fields = "__all__"
