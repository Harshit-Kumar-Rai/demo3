from rest_framework import serializers
from app.models.contact import (ContactDetails, Salutation)

class ContactDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactDetails
    fields = '__all__'
    
class SalutationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Salutation
    fields = '__all__'
    
