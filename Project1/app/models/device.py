from django.db import models
from .entity import EntityDetails


class DeviceDetails(models.Model):
  device_name  = models.CharField(max_length=100)
  entity_id = models.ForeignKey('EntityDetails', on_delete=models.CASCADE, blank=True, null=True, related_name='entitydetails')
  device_type_id = models.ForeignKey('DeviceType', on_delete=models.CASCADE, blank=True, null=True, related_name='devicetype')
  
  def __str__(self):
    return self.device_name

class DeviceType(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

class DeviceParameter(models.Model):
  pass

class DeviceParameterUnitDetails(models.Model):
  pass