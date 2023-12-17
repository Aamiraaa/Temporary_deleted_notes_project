from django.urls import path
from .views import NoteListCreateView, NoteRetrieveUpdateDeleteView, TempDeletedNoteListView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDeleteView.as_view(), name='note-retrieve-update-delete'),
    path('temp-deleted-notes/', TempDeletedNoteListView.as_view(), name='temp-deleted-note-list'),
]
