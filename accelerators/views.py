from django.shortcuts import render
from rest_framework.response import Response
from .serializers import AcceleratorSerializer
from rest_framework.views import APIView
import uuid
import base64
from django.core.files.base import ContentFile
from accelerators.models import Accelerator
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.


class AcceleratorView(APIView):

    def get(self, request):
        try:
            accelerators = Accelerator.objects.all()
            serializer = AcceleratorSerializer(accelerators, many=True)
            return Response({"status": "Sucess", "data": serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Error", "data": e.args[0]}, status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            acclerator = request.data
            acclerator["acc_img"] = self.base64_to_image(acclerator["acc_img"])
            acclerator["acc_logo"] = self.base64_to_image(
                acclerator["acc_logo"])
            serializer = AcceleratorSerializer(data=request.data, many=False)
            if (serializer.is_valid()):
                serializer.save()
                return Response({"status": "Sucess", "data": serializer.data}, status.HTTP_201_CREATED)
            else:
                return Response({"status": "Error", "data": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "Error", "data": e.args[0]}, status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            accelerators = Accelerator.objects.all()
            uid = kwargs["uid"]
            acc_id = get_object_or_404(accelerators, uuid=uid)
            acceleratorSerializer = AcceleratorSerializer(
                acc_id, data=request.data, many=False, partial=True)
            if acceleratorSerializer.is_valid():
                acceleratorSerializer.save()
                return Response({"status": "Success", "data": acceleratorSerializer.data}, status.HTTP_201_CREATED)
            else:
                return Response({"status": "Error", "data": acceleratorSerializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "Error", "data": e.args[0]}, status.HTTP_400_BAD_REQUEST)

    def base64_to_image(self, base64_string):
        format, imgstr = base64_string.split(';base64,')
        ext = format.split('/')[-1]
        return ContentFile(base64.b64decode(imgstr), name=uuid.uuid4().hex + "." + ext)
