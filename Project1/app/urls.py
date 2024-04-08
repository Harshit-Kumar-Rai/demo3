from django.urls import path
from app.views.custome_views import GetAllCityOfAddress, GetAllWardOfCities, GetAllStateOfCountry

urlpatterns = [
  path('get-city/<int:state_id>', GetAllCityOfAddress.as_view(), name='get-all-cities'),
  path('get-ward/<int:city_id>', GetAllWardOfCities.as_view(), name='get-all-wards'),
  path('get-state/<int:country_id>', GetAllStateOfCountry.as_view(), name= 'get-all-states')
]