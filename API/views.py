from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from API.serializers import UserSerializer

# Create your views here.

class UserListCreateView(APIView):

  def get(self, request):

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):

    #     # Register a new user
    #     serializer = UserSerializer(data=request.data)

    #     if serializer.is_valid():

    #         serializer.save()  # password is hashed in serializer

    #         return Response(status=status.HTTP_201_CREATED)
        
    #     return Response(status=status.HTTP_400_BAD_REQUEST)