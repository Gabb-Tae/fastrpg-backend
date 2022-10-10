from rest_framework.serializers import ModelSerializer
from core.models import rpgrace

class rpgraceSerializer(ModelSerializer):
    class Meta:
        model = rpgrace
        fields = "__all__"
