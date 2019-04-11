from accounts.models import User
from users.models import Feature
from users.models import Bank
from users.models import GeneralProfile
from users.models import Driver
from users.models import Setting
from users.models import Notifications
from users.models import Favorites
from users.models import Passenger
from users.models import Transmit
from users.models import Machine
from ticket.models import TicketEnvelope
from ticket.models import TicketLetter

from rest_framework.exceptions import NotAcceptable
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField

class UserNotificationsSerializer(ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('id', 'user', 'point_type', 'point', 'summary', 'seen')

class MachineFeaturesSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = ('name', 'status')

class MachineSerializer(ModelSerializer):
    features = SlugRelatedField(queryset = Feature.objects.all(), many = True, slug_field = 'name')

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
        fields = ('get_message_from', 'subscribe', 'email_transaction', 'email_trip_info')

class UserFavoritesSerializer(ModelSerializer):
    
    class Meta:
        model = Favorites
        fields = ('title', 'status', 'user')

class UserSerializer(ModelSerializer):
    profile = UserProfileSerializer(required = True)
    setting = UserSettingSerializer(required = True)
    favorites = UserFavoritesSerializer(required = True, many = True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'profile', 'favorites', 'setting')

class UserMainSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserRegisterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validate_data):
        try:
            first_name = validate_data['first_name']
            last_name = validate_data['last_name']
        except KeyError:
            raise NotAcceptable(detail = 'You need to fill all parameters.')
        user = User(
            email=validate_data['email'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name']
        )

        user.set_password(validate_data['password'])
        user.save()

        return user

class TicketSerializer(ModelSerializer):

    class Meta:
        model = TicketEnvelope
        fields = ('sku', 'subject', 'priority', 'status', 'department', 'trip', 'passenger', 'driver')
        read_only_fields = ('sku',)

class TicketLetterSerializer(ModelSerializer):

    class Meta:
        model = TicketLetter
        fields = ('sku', 'ticket', 'message', 'user', 'reply', 'created')
        read_only_fields = ('sku', 'created')