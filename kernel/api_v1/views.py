from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from django_filters import rest_framework as filters


from trip.models import City
from api_v1.serializers.trip.city import CitySerializer
from api_v1.serializers.trip.city import CityMainSerializer

from trip.models import Region
from api_v1.serializers.trip.region import RegionSerializer
from api_v1.serializers.trip.region import RegionMainSerilizer

from trip.models import Distance
from api_v1.serializers.trip.distance import DistanceSerializer
from api_v1.serializers.trip.distance import DistanceMainSerializer

from trip.models import Trip
from trip.models import Seat
from api_v1.serializers.trip.trip import TripSerializer
from api_v1.serializers.trip.trip import TripMainSerializer
from api_v1.serializers.trip.trip import SeatSerializer

from accounts.models import User
from users.models import GeneralProfile
from users.models import Driver
from users.models import Passenger
from users.models import Setting
from users.models import Transmit
from api_v1.serializers.users import UserSerializer
from api_v1.serializers.users import UserMainSerializer
from api_v1.serializers.users import UserProfileMainSerializer
from api_v1.serializers.users import UserProfileDriverMainSerializer
from api_v1.serializers.users import UserProfileTransmitMainSerializer
from api_v1.serializers.users import UserProfilePassengerMainSerializer
from api_v1.serializers.users import UserSettingSerializer

######## City ########

class APIListCreateCity(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityMainSerializer

class APIDetailCity(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class APIRetrieveUpdateCity(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CityMainSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

######## Region ########

class APIListCreateRegion(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionMainSerilizer

class APIRetrieveUpdateRegion(generics.RetrieveUpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionMainSerilizer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


######## DISTANCE ########

class APIListCreateDistance(generics.ListCreateAPIView):
    queryset = Distance.objects.all()
    serializer_class = DistanceMainSerializer

class APIDetailDistance(generics.ListAPIView):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer

class APIRetrieveUpdateDistance(generics.RetrieveUpdateAPIView):
    queryset = Distance.objects.all()
    serializer_class = DistanceMainSerializer
    lookup_field = 'url'
    lookup_url_kwarg = 'url'


######################
######## USER ########
######################

class APIListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserMainSerializer


class APIDetailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
    lookup_url_kwarg = 'email'

class APIRetrieveUpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserMainSerializer
    lookup_field = 'email'
    lookup_url_kwarg = 'email'

#### Profile

class APIRetrieveUpdateUserProfile(generics.RetrieveUpdateAPIView):
    queryset = GeneralProfile.objects.all()
    serializer_class = UserProfileMainSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class APIRetrieveUpdateUserSetting(generics.RetrieveUpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = UserSettingSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'
    

class APIRetrieveUpdateUserProfileDriver(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = UserProfileDriverMainSerializer
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserProfilePassenger(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = UserProfilePassengerMainSerializer
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserProfileTransmit(generics.RetrieveUpdateAPIView):
    queryset = Transmit.objects.all()
    serializer_class = UserProfileTransmitMainSerializer
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

######################
######## Trip ########
######################

class APIListCreateTrip(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripMainSerializer

class APIRetrieveTrip(generics.RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class APIRetrieveUpdateTrip(generics.RetrieveUpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripMainSerializer

class APIListTripSeat(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('trip', )

class APIRetrieveUpdateSeats(generics.RetrieveUpdateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

