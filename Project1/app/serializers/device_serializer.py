from rest_framework import serializers
from app.models.device import (DeviceDetails, DeviceType)

class DeviceDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceDetails
    fields = '__all__'
    
class DeviceTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceType
    fields = "__all__"