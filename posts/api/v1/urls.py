from django.urls import path
from .views import CategoriesView, CategoryDetailView, PostDetailView                

urlpatterns = [
    # Category enpoints
    path('v1/categories/', CategoriesView.as_view(), name='categories'),
    path('v1/categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    # Post endpoints
    # path('v1/posts/', '', name='posts'),
    path('v1/posts/<int:id>/', PostDetailView.as_view(), name='post-detail')
]