from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from API.serializers import UserRegisterSerializer

class UserRegisterView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)  
        return Response(serializer.data)
    
    # def post(self,request):

    #     serializer = UserRegisterSerializer(data = request.data)

    #     if serializer.is_valid():

    #         serializer.save()    

    #         return Response(status=status.HTTP_201_CREATED)
        
    #     return Response(status=status.HTTP_400_BAD_REQUEST)