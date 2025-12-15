from django.shortcuts import render
from api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.



class UserRegisterApi(APIView):

    def get(self, request):

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()  

            return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class ReteievUpadateDeleteViwe(APIView):

    def get(self, request, **kwargs):

        id = kwargs.get('pk')

        user = get_object_or_404(User, id = id)

        Serializer = UserSerializer(user)

        return Response(Serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, **kwargs):

        id = kwargs.get('pk')

        user =  get_object_or_404(User, id = id)

        serializer = UserSerializer(user, data = request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):

        id = kwargs.get('pk')

        user = get_object_or_404(User, id = id)

        user.delete()

        return Response({"message":"Object deleted successfully"}, status=status.HTTP_200_OK)






    
   
    