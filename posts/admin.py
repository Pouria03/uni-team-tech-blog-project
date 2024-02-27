from django.contrib import admin
from posts.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ('titile', 'content')
    list_filter = ('category',)


class CategoryAdmin(PostAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, PostAdmin)
