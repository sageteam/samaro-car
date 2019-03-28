from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import CitySerializer
from .serializers import DistanceSerializer
from .serializers import RegionSerializer
from .serializers import TripSerializer

from trip.models import City
from trip.models import Trip
from trip.models import Distance
from trip.models import Region


class APIListCreateCity(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class APIRetrieveUpdateDestroyCity(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class APIListCreateRegion(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
class APIRetrieveUpdateDestroyRegion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class APIListCreateDistance(generics.ListCreateAPIView):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer
    
class APIRetrieveUpdateDestroyDistance(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer
    lookup_field = 'url'
    lookup_url_kwarg = 'url'


class APIListCreateTrip(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    