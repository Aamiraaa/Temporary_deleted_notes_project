from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Note, TempDeletedNote
from .serializers import NoteSerializer, TempDeletedNoteSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.filter(is_deleted=False)
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save()

class NoteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        TempDeletedNote.objects.create(note=instance)

class TempDeletedNoteListView(generics.ListAPIView):
    queryset = TempDeletedNote.objects.all()
    serializer_class = TempDeletedNoteSerializer
