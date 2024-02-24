from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterUserSerializer



class RegisterUserView(APIView):
    """ This API View conducts the process of registering user"""
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
