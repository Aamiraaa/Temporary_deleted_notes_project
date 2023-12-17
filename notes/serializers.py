from rest_framework import serializers
from .models import Note, TempDeletedNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class TempDeletedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempDeletedNote
        fields = '__all__'
