from rest_framework.serializers import ModelSerializer
from trip.models import City
from trip.models import Distance
from trip.models import Region
from trip.models import Seat
from trip.models import Trip

class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name',)

class CitySerializer(ModelSerializer):
    region = RegionSerializer(required = True)

    class Meta:
        model = City
        fields = ('id', 'name', 'region',)

class DistanceSerializer(ModelSerializer):
    city1 = CitySerializer(required = True)
    city2 = CitySerializer(required = True)
    across = CitySerializer(required = True, many = True)

    class Meta:
        model = Distance
        fields = ('city1', 'city2', 'url', 'road', 'across', 'price', 'distance')
        read_only_fields = ('slug', 'price',)

class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = ('position', 'state', 'init_price', 'paid_price', 'type_price', 'discount', 'user', 'trip')


class TripSerializer(ModelSerializer):
    origin = CitySerializer(required = True)
    destination = CitySerializer(required = True)
    origin_region = RegionSerializer(required = True)
    destination_region = RegionSerializer(required = True)
    seats = SeatSerializer(required = True)
    class Meta:
        model = Trip
        fields = ('origin', 'origin_region', 'destination', 'destination_region', 'driver', 'seats', 'status', 'gender', 'active', 'start_time')
        

