from rest_framework import serializers
from posts.models import Category

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
            }
        }
        
    def get_subcategories(self, obj):
        if obj.parent is None:
            return CategorySerializer(obj.category_set.all(), many=True).data
        else:
            return []

