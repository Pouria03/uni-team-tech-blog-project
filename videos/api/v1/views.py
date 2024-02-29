from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import (generics,
                            status,
                            filters
                        )
from django.db.models import Q
from videos.models.tag import Tag
from .serializers import VideoSerializer, TagDetailSerializer
from videos.models import Video
from helpers.paginations import CustomPageNumberPagination


class VideoListView(APIView):
    """
    This View gets all videos with their tags.
    the result also includes filtering, search and pagination
    """
    def get(self, request):
        videos = Video.objects.get_actives()
        filter_params = self.request.query_params.getlist('tags', [])
        search_param = request.query_params.get('search')
        if search_param:
            videos = videos.filter(Q(title__icontains=search_param)|
                                   Q(description__icontains=search_param))
            
        if filter_params:
            videos = videos.filter(tags__id__in=filter_params)

        paginator = CustomPageNumberPagination()
        paginated_videos = paginator.paginate_queryset(videos, request)
        serializer = VideoSerializer(paginated_videos, many=True)
        data = {}
        return paginator.get_paginated_response(serializer.data)



class VideoDetailView(APIView):
    """
    This View gets one video object and its associated tags and comments by video's ID.
    """
    serializer_class = VideoSerializer
    def get(self, request, id):
        # TODO : get comments
        video = get_object_or_404(Video, id=id, is_active=True)
        serializer = VideoSerializer(video)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class TagDetailView(APIView):
    """
    This View class gets id of a tag and returns the tag's detail,
    including videos related to the tag.
    """
    def get(self, request, id):
        tag = get_object_or_404(Tag, id=id)
        serializer = TagDetailSerializer(tag)
        return Response(data=serializer.data, status=status.HTTP_200_OK)        