from rest_framework.serializers import ModelSerializer, CharField

from project.models import Project
from user.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        repository = CharField(max_length=128, required=False)
        fields = '__all__'
