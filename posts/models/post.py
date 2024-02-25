from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to='post_image_uploads/')
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(db_default=True)
    categories = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title
