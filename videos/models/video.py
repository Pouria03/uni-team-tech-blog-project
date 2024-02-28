from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class VideoManager(models.Manager):
    def get_actives(self):
        return super().get_queryset().filter(is_active='True')


class Video(models.Model):
    title = models.CharField(max_length=90)
    description = RichTextField()
    file = models.FileField(upload_to='video_files_uploads/')
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self) -> str:
        return self.title
