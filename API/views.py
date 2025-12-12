from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from API.serializers import UserSerializer

# Create your views here.

class UserListCreateView(APIView):

    def get(self, request): 

        # List all users
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)