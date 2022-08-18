from rest_framework.relations import StringRelatedField, SlugRelatedField
from rest_framework.serializers import ModelSerializer

from todo_notes.models import TODO_Note


class TODO_NoteModelSerializer(ModelSerializer):
    project = SlugRelatedField(slug_field='name', read_only=True)
    user = StringRelatedField()

    class Meta:
        model = TODO_Note
        fields = '__all__'
