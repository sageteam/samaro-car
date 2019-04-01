from trip.models import Region, City
from rest_framework.serializers import ModelSerializer

class RegionSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = ('name',)

class RegionMainSerilizer(ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'name', 'city', 'is_traditional')
