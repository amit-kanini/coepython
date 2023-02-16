from django.shortcuts import render
from rest_framework.response import Response
from user.serializers import UserSerializer
from rest_framework.views import APIView
import uuid
import base64
from django.core.files.base import ContentFile
from user.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class UserView(APIView):
    def get(self,request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({"status": "Sucess", "data": serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Error", "data": e.args[0]}, status.HTTP_400_BAD_REQUEST)


    def post(self,request):
        try:
            serializer = UserSerializer(data=request.data, many=False)
            if (serializer.is_valid()):
                serializer.save()
                return Response({"status": "Sucess", "data": serializer.data}, status.HTTP_201_CREATED)
            else:
                return Response({"status": "Error", "data": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "Error", "data": e.args[0]}, status.HTTP_400_BAD_REQUEST)



