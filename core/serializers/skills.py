from rest_framework.serializers import ModelSerializer
from core.models import skills

class skillsSerializer(ModelSerializer):
    class Meta:
        model = skills
        fields = "__all__"
