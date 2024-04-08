from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from app.views import AddressDetailsViewSet
from app.views.entity_views import EntityDetailsViewSet #, EntityAddressAndContactViewSet
from app.views.address_views import AddressDetails
from app.views.contact_views import ContactViewSet

router = DefaultRouter()
router.register('entity', EntityDetailsViewSet, basename='entity')
router.register('address', AddressDetails, basename='address')
router.register('contact', ContactViewSet, basename='contact')
#router.register('full-details', EntityAddressAndContactViewSet, basename='fulldetails')
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("filter-api/", include('app.urls'))
]
