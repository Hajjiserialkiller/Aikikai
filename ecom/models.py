from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField()
    video_uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

