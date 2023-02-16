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


class LoginView(APIView):
    pass
    # def post(self, request):
    #     userEmail = request.data["email"]
    #     userPassword = request.data["password"]
    #     users = User.objects.all()
    #     user = users.filter(
    #         email == userEmail and password == userPassword)
    #     print(user)
    #     if (user):
    #         return Response({"status": "Sucess"}, status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "Error"}, status.HTTP_400_BAD_REQUEST)
    #     #serializer = UserSerializer(users, many=True)
