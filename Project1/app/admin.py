from django.contrib import admin
from .models.entity import (EntityDetails, EntityRoleID, EntityTypeID)
from .models.address import (AddressDetails, AddressType, City, State, Country, Ward, Zone)
from .models.contact import (ContactDetails, Salutation)
from .models.device import(DeviceDetails, DeviceType)


admin.site.register(EntityDetails)
admin.site.register(EntityRoleID)
admin.site.register(EntityTypeID)

admin.site.register(AddressDetails)
admin.site.register(AddressType)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Ward)
admin.site.register(Zone)

admin.site.register(ContactDetails)
admin.site.register(Salutation)

admin.site.register(DeviceDetails)
admin.site.register(DeviceType)
