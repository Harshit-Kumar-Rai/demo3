from django.db import models
from app.models.address import *
# contact details

class ContactDetails(models.Model):
  saluation_id = models.ForeignKey('Salutation', on_delete=models.CASCADE, blank=True, null=True, related_name='saluation')
  first_name = models.CharField(max_length=100)
  last_name  = models.CharField(max_length=100)
  address_id = models.ForeignKey('AddressDetails', on_delete=models.CASCADE, blank=True, null=True, related_name='address')
  image = models.ImageField(upload_to = 'media',blank=True,null=True)
  
  def __str__(self):
    return self.first_name

class Salutation(models.Model):
  name =  models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class SocialMeida(models.Model):
  pass