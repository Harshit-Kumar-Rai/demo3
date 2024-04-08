from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers.address_serializer import CitySerializer, WardSerializer, StateSerializer
from app.models.address import City, Ward, State

class GetAllCityOfAddress(APIView):
  def get(self, request, state_id):
    cities = City.objects.filter(state_id = state_id)
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)
  
class GetAllWardOfCities(APIView):
  def get(self,request,city_id):
    wards = Ward.objects.filter(city_id = city_id)
    serializer = WardSerializer(wards,many=True)
    return Response(serializer.data)
  
class GetAllStateOfCountry(APIView):
  def get(self, request, country_id):
    states = State.objects.filter(country_id = country_id).order_by('-name')
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)