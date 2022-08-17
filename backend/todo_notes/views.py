from rest_framework.viewsets import ModelViewSet

from todo_notes.models import TODO_Note
from todo_notes.serializers import TODO_NoteModelSerializer


class TODO_NoteModelViewSet(ModelViewSet):
    serializer_class = TODO_NoteModelSerializer
    queryset = TODO_Note.objects.all()
