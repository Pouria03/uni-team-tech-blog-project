from django.urls import path
from .views import CategoriesView, CategoryDetailView

urlpatterns = [
    path('v1/categories/', CategoriesView.as_view(), name='categories'),
]