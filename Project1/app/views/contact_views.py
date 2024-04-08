from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import  status
from app.models.contact import *
from app.serializers.contact_serializer import ContactDetailsSerializer

class ContactViewSet(viewsets.ModelViewSet):
  queryset = ContactDetails.objects.all()
  serializer_class = ContactDetailsSerializer
  