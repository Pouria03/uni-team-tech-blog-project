from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Category
from posts.api.v1.serializers import CategorySerializer
from posts.api.v1.permissions import StaffOrSuperuserPermission


class CategoriesView(APIView):
    permission_classes = [StaffOrSuperuserPermission]
    def post(self, request):
        """Create a category (category or sub category)"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Get all Categories"""
        categories = Category.objects.prefetch_related('parent').filter(parent=None)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

