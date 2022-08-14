from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from project.models import Project
from project.serializers import ProjectModelSerializer


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
