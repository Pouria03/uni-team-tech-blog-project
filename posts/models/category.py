from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    short_description = models.CharField(max_length=90, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True,
        related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # prevent a category to be itself parent
        if self.id and self.parent and self.id == self.parent.id:
            self.parent = None
        super().save(*args, **kwargs)