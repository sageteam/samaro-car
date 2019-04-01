from rest_framework.serializers import ModelSerializer
from accounts.models import User
from trip.models import City
from trip.models import Distance
from trip.models import Region
from trip.models import Seat
from trip.models import Trip
from users.models import Driver
from users.models import GeneralProfile
from users.models import Passenger
from users.models import Transmit
from users.models import Favorites
from users.models import Setting
from users.models import Machine
from users.models import Feature
from users.models import Bank


class MachineFeaturesSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = ('name', 'status')

class MachineSerializer(ModelSerializer):
    features = MachineFeaturesSerializer(required = True, many = True)

    class Meta:
        model = Machine
        fields = ('name', 'color', 'model', 'plaque', 'year', 'chassis_number', 'driver_card', 'machine_card', 'misdiagnosis', 'car_pic', 'features')

class BankSerializer(ModelSerializer):

    class Meta:
        model = Bank
        fields = ('bank_acc_name', 'bank_name', 'bank_sheba', 'bank_card')

class UserProfileDriverSerializer(ModelSerializer):
    machine = MachineSerializer(required = True)
    bank = BankSerializer(required = True)

    class Meta:
        model = Driver
        fields = ('job', 'job_place', 'emergency_number', 'machine', 'bank')

class UserProfileSerializer(ModelSerializer):
    driver = UserProfileDriverSerializer(required = True)
    
    class Meta:
        model = GeneralProfile
        fields = ('gender', 'birth_date', 'national_code', 'tel', 'mobile', 'adr', 'postal_code', 'pic', 'national_code_pic', 'edu_degree', 'about', 'driver')

class UserSettingSerializer(ModelSerializer):
    
    class Meta:
        model = Setting
        fields = ('__all__')

class UserSerializer(ModelSerializer):
    profile = UserProfileSerializer(required = True)
    setting = UserSettingSerializer(required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile', 'favorites', 'setting')

class UserFavoritesSerializer(ModelSerializer):
    user = UserSerializer(required = True)

    class Meta:
        model = Favorites
        fields = ('title', 'status')


class RegionSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'name',)


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
    seat = SeatSerializer(required = True, many = True)
    
    driver = UserSerializer(required = True)

    class Meta:
        model = Trip
        fields = ('origin', 'origin_region', 'destination', 'destination_region', 'driver', 'seat', 'status', 'gender', 'active', 'start_time')

