from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import  status

from app.serializers.address_serializer import (AddressDetailsSerializer, AddressTypeSerializer, CitySerializer, StateSerializer, ContrySerializer, WardSerializer, ZoneSerializer)
from app.models.address import (AddressDetails, AddressType, City, State, Country, Ward, Zone)


class AddressDetails(viewsets.ModelViewSet):
  queryset = AddressDetails.objects.all() 
  serializer_class = AddressDetailsSerializer
