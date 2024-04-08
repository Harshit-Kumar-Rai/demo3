from django.db import models

class EntityDetails(models.Model):
  name = models.CharField(max_length=150)
  short_name = models.CharField(max_length=100)
  long_name = models.CharField(max_length=300)
  trade_name = models.CharField(max_length=100)
  type_id = models.ForeignKey('EntityTypeID', on_delete=models.CASCADE, blank=True, null=True, related_name='MasterEntityTypeID') # This is the entity's role
  role_id = models.ForeignKey('EntityRoleID', on_delete=models.CASCADE, blank=True, null=True, related_name='MasterEntityRoleID') # This is role id 
  
  def __str__(self):
    return self.name

class EntityTypeID(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class EntityRoleID(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

