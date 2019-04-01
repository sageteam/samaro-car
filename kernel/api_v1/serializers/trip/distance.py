from trip.models import Distance
from api_v1.serializers.trip.city import CitySerializer
from api_v1.serializers.trip.region import RegionSerializer
from rest_framework.serializers import ModelSerializer

class DistanceSerializer(ModelSerializer):
    city1 = CitySerializer(required = True)
    city2 = CitySerializer(required = True)
    across = CitySerializer(required = True, many = True)

    class Meta:
        model = Distance
        fields = ('url', 'city1', 'city2', 'road', 'across', 'price', 'distance')
        read_only_fields = ('slug', 'price',)

class DistanceMainSerializer(ModelSerializer):

    class Meta:
        model = Distance
        fields = ('url', 'city1', 'city2', 'road', 'across', 'price', 'distance')
        read_only_fields = ('url', 'price',)