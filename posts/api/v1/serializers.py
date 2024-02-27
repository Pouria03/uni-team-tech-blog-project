from rest_framework import serializers
from posts.models import Category, Post
from django.contrib.auth import get_user_model

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    """ This serializer is used to in CRUD operation """
    subcategories = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id', 'title', 'short_description', 'parent', 'subcategories')
        extra_kwargs = {
            'parent': {
                'help_text': 'enter the ID of parent category (optional)'
            },
            'subcategories': {
                'read_only': True
            },
            'id': {
                'read_only': True
            }
        }
        
    def get_subcategories(self, obj):
        if obj.parent is None:
            return CategorySerializer(obj.category_set.all(), many=True).data
        else:
            return []
        

class PostSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all(),
        allow_null=True,
        required=True
    )
    category = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Category.objects.all(),
        allow_null=True,
        required=True
    )
    class Meta:
        model = Post
        fields = ['title', 'date_created', 'content', 'thumbnail', 'writer', 'category', 'is_active']
        extra_kwargs = {
            'date_created' : {
                'read_only' : True
            }
        }

    # TODO: get all comments for each post
    def get_comments(self, obj):
        pass


