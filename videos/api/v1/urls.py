from django.urls import path
from .views import (VideoListView,
                    VideoDetailView,
                    TagDetailView,
                    
                )
urlpatterns = [
    path('v1/videos/', VideoListView.as_view(), name='videos'),
    path('v1/videos/<int:id>/', VideoDetailView.as_view(), name='videos-detail'),
    path('v1/tags/<int:id>/', TagDetailView.as_view(), name='tags-detail'),
]