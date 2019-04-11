from trip.models import Distance
from trip.models import City
from api_v1.serializers.trip.city import CitySerializer
from api_v1.serializers.trip.region import RegionSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField


class DistanceSerializer(ModelSerializer):
    city1 = SlugRelatedField(queryset = City.objects.all(), slug_field='name')
    city2 = SlugRelatedField(queryset = City.objects.all(), slug_field = 'name')
    across = SlugRelatedField(queryset = City.objects.all(), many = True, slug_field='name')

    class Meta:
        model = Distance
        fields = ('url', 'city1', 'city2', 'across', 'road', 'price', 'distance')
        read_only_fields = ('url', 'price', 'across')
        
