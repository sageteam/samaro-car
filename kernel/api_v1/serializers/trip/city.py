from trip.models import City
from api_v1.serializers.trip.region import RegionSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField


class CitySerializer(ModelSerializer):
    regions = SlugRelatedField(many = True, read_only = True, slug_field='name')
    class Meta:
        model = City
        fields = ('pk', 'name', 'regions')
