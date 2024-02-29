from rest_framework import serializers
from videos.models import Video, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')


class VideoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = ('title', 'description', 'file', 'tags')


class TagDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = ('id', 'name', 'videos')
        
