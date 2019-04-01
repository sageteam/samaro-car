from accounts.models import User
from users.models import Feature
from users.models import Bank
from users.models import GeneralProfile
from users.models import Driver
from users.models import Setting
from users.models import Notifications
from users.models import Passenger
from users.models import Transmit
from users.models import Machine


from rest_framework.serializers import ModelSerializer


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

class UserProfileDriverMainSerializer(ModelSerializer):

    class Meta:
        model = Driver
        fields = ('job', 'job_place', 'emergency_number')

class UserProfilePassengerMainSerializer(ModelSerializer):

    class Meta:
        model = Passenger
        fields = ('job', 'emergency_number')

class UserProfileTransmitMainSerializer(ModelSerializer):

    class Meta:
        model = Transmit
        fields = ('job', 'emergency_number')

class UserProfileTransmitSerializer(ModelSerializer):
    class Meta:
        model = Transmit
        fields = ('job', 'emergency_number')

class UserProfilePassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('job', 'emergency_number')

class UserProfileSerializer(ModelSerializer):
    driver = UserProfileDriverSerializer(required = True)
    passenger = UserProfilePassengerSerializer(required = True)
    transmit = UserProfileTransmitSerializer(required = True)
    
    class Meta:
        model = GeneralProfile
        fields = ('gender', 'birth_date', 'national_code', 'tel', 'mobile', 'adr', 'postal_code', 'pic', 'national_code_pic', 'edu_degree', 'about', 'driver', 'transmit', 'passenger')

class UserProfileMainSerializer(ModelSerializer):
    
    class Meta:
        model = GeneralProfile
        fields = ('gender', 'birth_date', 'national_code', 'tel', 'mobile', 'adr', 'postal_code', 'pic', 'national_code_pic', 'edu_degree', 'about')


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

class UserMainSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'id')

