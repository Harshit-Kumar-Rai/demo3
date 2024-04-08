from rest_framework import serializers
from app.models.entity import (EntityDetails, EntityTypeID, EntityRoleID)
# from app.serializers.address_serializer import AddressDetailsSerializer
from app.serializers.contact_serializer import ContactDetailsSerializer
from app.models.address import AddressDetails
from app.models.contact import ContactDetails

class EntityDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityDetails
    fields = '__all__'
    
class EntityTypeIDSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityTypeID
    fields = '__all__'
    
class EntityRoleIDSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityRoleID
    fields = '__all__'
    
    
# class EntityWithAddressAndContactDetails(serializers.ModelSerializer):
#   # address = AddressDetailsSerializer(many=True)
#   # contacts = ContactDetailsSerializer(many=True)
  
#   # Use string import for AddressDetailsSerializer and ContactDetailsSerializer
#   # 2nd appproac not working
#   address = 'app.serializers.address_serializer.AddressDetailsSerializer'(many=True)
#   contacts = 'app.serializers.contact_serializer.ContactDetailsSerializer'(many=True)
  
  
#   class Meta:
#     model = EntityDetails
#     fields = '__all__'
    
#   def create(self, validated_data):
    
#     address_data = validated_data.pop('address')
#     contacts_data = validated_data.pop('contacts')
#     entity = EntityDetails.objects.create(**validated_data)
    
#     for address_data in address_data:
#       AddressDetails.objects.create(entity=entity, **address_data)
#     for contacts_data in contacts_data:
#       AddressDetails.objects.create(entity=entity, **address_data)
      
#     return entity 

# Overriding the update method to handle nested serialization of data
# This is because DRF does not support PUT/PATCH on nested resources by default
