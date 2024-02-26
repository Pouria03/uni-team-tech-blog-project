from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from posts.models import Category
from posts.api.v1.serializers import CategorySerializer
from posts.api.v1.permissions import StaffOrSuperuserPermission


class CategoriesView(APIView):
    serializer_class = CategorySerializer
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
        """Get all Categories with their subcategories"""
        categories = Category.objects.prefetch_related('parent').filter(parent=None)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):
    serializer_class = CategorySerializer
    permission_classes = [StaffOrSuperuserPermission]
    def setup(self, request, *args, **kwargs):
        """This method gets the exact object related to ID that is entered through enpoint"""
        self.this_category = get_object_or_404(Category, id=kwargs['id'])
        return super().setup(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """This method updates attributes of a category or sub category"""
        serializer = CategorySerializer(data=request.data, instance=self.this_category, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """This method deletes a category or a sub category"""
        try:
            category_title = self.this_category.title
            self.this_category.delete()
            return Response({"result":"{} deleted successfully".format(category_title)}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"result":"Not found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"result":"Something went wrong. Try again later"}, status=status.HTTP_400_BAD_REQUEST)