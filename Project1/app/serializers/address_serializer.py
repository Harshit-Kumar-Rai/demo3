from rest_framework import serializers
from app.models.address import (AddressDetails, AddressType, City, State, Country, Ward, Zone)
from .entity_serializer import EntityDetailsSerializer

# class AddressDetailsSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = AddressDetails
#     fields = '__all__'
    
class AddressTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddressType
    fields = ['id', 'address_type', 'remarks']
    
class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['id', 'name', 'state_id'] #ward id removed
    
class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = ['id', 'name', 'country_id']
    
class ContrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = ['id', 'name']
    
class WardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ward
    # fields = ['id', 'name', 'zone_id', 'city_id']
    fields = '__all__'
    
class ZoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Zone
    fields = ['id', 'name']
    
class AddressDetailsSerializer(serializers.ModelSerializer):
  entity = EntityDetailsSerializer(many=True, required=False)
  address_type = AddressTypeSerializer(many=True, required=False)
  country = ContrySerializer(many=True, required=False)
  state = StateSerializer(many=True, required=False)
  city = CitySerializer(many=True, required=False)
  ward = WardSerializer(many=True, required=False)
  zone = ZoneSerializer(many=True, required=False)
  
  class Meta:
    model = AddressDetails
    # fields = ['id', 'address_type', 'country', 'state', 'city', 'ward', 'zone']
    fields = '__all__'