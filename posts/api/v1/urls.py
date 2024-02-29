from django.urls import path
from .views import CategoriesView, CategoryDetailView, PostDetailView , PostsView               

urlpatterns = [
    path('v1/categories/', CategoriesView.as_view(), name='categories'),
    # path('v1/categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('v1/posts/', PostsView.as_view(), name='posts'),
    path('v1/posts/<int:id>/', PostDetailView.as_view(), name='post-detail')
]