from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from todo_notes.models import TODO_Note
from todo_notes.serializers import TODO_NoteModelSerializer


class TODO_NoteLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TODO_NoteModelLimitedViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):

    pagination_class = TODO_NoteLimitOffsetPagination
    serializer_class = TODO_NoteModelSerializer
    queryset = TODO_Note.objects.all()

    def perform_destroy(self, instance):
        instance.active = "false"
        instance.save()

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            return TODO_Note.objects.filter(project=project_id)
        return TODO_Note.objects.all()
