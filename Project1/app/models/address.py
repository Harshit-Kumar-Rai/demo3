from django.db import models
from .entity import EntityDetails
# Address Details

class AddressDetails(models.Model):
  entity_id = models.ForeignKey('EntityDetails', on_delete=models.CASCADE, blank=True, null=True, related_name='addressentitydetails')
  aaddress_type_id = models.ForeignKey('AddressType', on_delete=models.CASCADE, blank=True, null=True, related_name='addresstype')
  country_id = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True, related_name='mastercountry')
  state_id = models.ForeignKey('State', on_delete=models.CASCADE, blank=True, null=True, related_name='masterstate')
  city_id = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True, related_name='city')
  zone_id = models.ForeignKey('Zone', on_delete=models.CASCADE, blank=True, null=True, related_name='masterzone')
  ward_id = models.ForeignKey('Ward', on_delete=models.CASCADE, blank=True, null=True, related_name='masterward')
  line1 = models.CharField(max_length=100, blank=True,null=True)
  line2 = models.CharField(max_length=100, blank=True, null=True)
  
  def __str__(self):
    if self.line1:
      return self.line1
    else:
      return str(self.pk)

class AddressType(models.Model):
  address_type = models.CharField(max_length=100)
  remarks = models.CharField(max_length=1000)
  
  def __str__(self):
    return self.address_type

class City(models.Model):
  name = models.CharField(max_length=80)
  state_id = models.ForeignKey('State', on_delete=models.CASCADE, blank=True, null=True, related_name='state')
  # ward_id = models.ForeignKey('Ward', on_delete=models.CASCADE, blank=True, null=True, related_name='ward')

  def __str__(self):
    return self.name
  
class State(models.Model):
  name = models.CharField(max_length=100)
  country_id = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True, related_name='statecountry')
  
  def __str__(self):
    return self.name

class Country(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Ward(models.Model):
  name = models.CharField(max_length=100)
  city_id = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True, related_name='ward_city')
  zone_id = models.ForeignKey('Zone', on_delete=models.CASCADE, blank=True, null=True, related_name='zone')
  
  def __str__(self):
    return self.name

class Zone(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name