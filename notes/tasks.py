from celery import shared_task
from django.utils import timezone
from .models import Note

@shared_task
def delete_notes_older_than_four_hours():
    four_hours_ago = timezone.now() - timezone.timedelta(hours=1)
    notes_to_delete = Note.objects.filter(created_at__lte=four_hours_ago)
    notes_to_delete.delete()