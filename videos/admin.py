from django.contrib import admin
from videos.models import Video, Tag


# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    list_filter = ('tags', )


admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)