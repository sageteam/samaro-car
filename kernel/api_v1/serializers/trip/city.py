from trip.models import City
from trip.models import Region
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class CitySerializer(ModelSerializer):
    regions = RegionSerializer(many = True, read_only = True)
    class Meta:
        model = City
        fields = ('pk', 'name', 'regions')
