from rest_framework import serializers
                                       
from accelerators.models import Accelerator


class AcceleratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accelerator
        fields = "__all__"