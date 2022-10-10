from rest_framework.serializers import ModelSerializer
from core.models import itens

class itensSerializer(ModelSerializer):
    class Meta:
        model = itens
        fields = "__all__"
