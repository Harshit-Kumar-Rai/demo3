from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import  status
from ..serializers.entity_serializer import EntityDetailsSerializer, EntityRoleID, EntityTypeID #, EntityWithAddressAndContactDetails
from ..models.entity import EntityDetails, EntityTypeID, EntityRoleID


class EntityDetailsViewSet(viewsets.ModelViewSet):
  queryset = EntityDetails.objects.all()
  serializer_class = EntityDetailsSerializer
  
# class EntityAddressAndContactViewSet(viewsets.ModelViewSet):
#     queryset = EntityDetails.objects.all()
#     serializer_class = EntityWithAddressAndContactDetails