from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination

from project.models import Project
from project.serializers import ProjectModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelLimitedViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet):

    pagination_class = ProjectLimitOffsetPagination
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            return Project.objects.filter(name__icontains=name)
        return Project.objects.all()
