from trip.models import City
from api_v1.serializers.trip.region import RegionSerializer
from rest_framework.serializers import ModelSerializer

class CitySerializer(ModelSerializer):
    regions = RegionSerializer(required = True, many = True)

    class Meta:
        model = City
        fields = ('name', 'regions',)
        read_only_fields = ('regions',)

class CityMainSerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', )
        