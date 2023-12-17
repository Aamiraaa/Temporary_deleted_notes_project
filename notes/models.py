from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

class TempDeletedNote(models.Model):
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(default=timezone.now)
