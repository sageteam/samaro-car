from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ReturnDict
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from django_filters import rest_framework as filters

from trip.models import City
from api_v1.serializers.trip.city import CitySerializer

from trip.models import Region
from api_v1.serializers.trip.region import RegionSerializer

from trip.models import Distance
from api_v1.serializers.trip.distance import DistanceSerializer


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
from users.models import Machine
from users.models import Favorites
from users.models import Feature
from users.models import Notifications
from users.models import Bank

from dashboard.models import Rules
from dashboard.models import RulesCategory
from dashboard.models import FAQ
from dashboard.models import FAQCategory

from ticket.models import TicketEnvelope
from ticket.models import TicketLetter

from api_v1.serializers.users import UserSerializer
from api_v1.serializers.users import UserMainSerializer
from api_v1.serializers.users import UserSettingSerializer
from api_v1.serializers.users import UserFavoritesSerializer
from api_v1.serializers.users import UserProfileMainSerializer
from api_v1.serializers.users import UserProfileDriverMainSerializer
from api_v1.serializers.users import UserProfileTransmitMainSerializer
from api_v1.serializers.users import UserProfilePassengerMainSerializer
from api_v1.serializers.users import MachineSerializer
from api_v1.serializers.users import MachineFeaturesSerializer
from api_v1.serializers.users import BankSerializer
from api_v1.serializers.users import UserNotificationsSerializer
from api_v1.serializers.users import UserRegisterSerializer
from api_v1.serializers.users import TicketSerializer 
from api_v1.serializers.users import TicketLetterSerializer

from api_v1.serializers.dashboard.faq import FAQSerializer
from api_v1.serializers.dashboard.faq import FAQCategorySerializer
from api_v1.serializers.dashboard.rules import RulesSerializer
from api_v1.serializers.dashboard.rules import RulesCategorySerializer

from .permissions import NoPermission
from .permissions import NormalPermission
from .permissions import RegisterPermission
from .permissions import UserPermission
from .permissions import UserMachinePermission
from .permissions import UserNestedProfilePermission
from .permissions import UserProfilePermission

######## Ticket ########
class TicketViewSet(viewsets.ModelViewSet):
    queryset = TicketEnvelope.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'sku'
    lookup_url_field = 'sku'

class TicketLetterViewSet(viewsets.ModelViewSet):
    queryset = TicketLetter.objects.all()
    serializer_class = TicketLetterSerializer
    lookup_field = 'sku'
    lookup_url_field = 'sku'

######## City ########
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [NormalPermission]
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


######## Region ########
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [NormalPermission]
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


######## DISTANCE ########
class DistanceViewSet(viewsets.ModelViewSet):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer
    permission_classes = [NormalPermission]
    lookup_field = 'road'
    lookup_url_kwarg = 'road'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city1', 'city2', 'road')

######## Dashboard ########
class RulesViewSet(viewsets.ModelViewSet):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class RulesCategoryViewSet(viewsets.ModelViewSet):
    queryset = RulesCategory.objects.all()
    serializer_class = RulesCategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class FAQCategoryViewSet(viewsets.ModelViewSet):
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


######################
######## USER ########
######################

class APIDetailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (UserPermission,)
    lookup_field = 'email'
    lookup_url_kwarg = 'email'

#### Authentication

class APILoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer
    permission_classes = (NoPermission,)
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return ObtainAuthToken().post(request)

class APIRegisterViewSet(APIView):
    permission_classes = (NoPermission,)
    def post(self, request, format = None, *args, **kwargs):
        
        serializer = UserRegisterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
#### Profile

class APIRetrieveUpdateUserProfile(generics.RetrieveUpdateAPIView):
    queryset = GeneralProfile.objects.all()
    serializer_class = UserProfileMainSerializer
    permission_classes = (UserProfilePermission,)
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class APIRetrieveUpdateUserSetting(generics.RetrieveUpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = UserSettingSerializer
    permission_classes = (UserProfilePermission,)
    lookup_field = 'user'
    lookup_url_kwarg = 'user'
    
class APIFavoites(APIView):
    permission_classes = (UserPermission,)
    

    def get(self, request, format = None, *args, **kwargs):
        user_pk = kwargs['user']
        favorites = Favorites.objects.filter(user = user_pk)
        serializer = UserFavoritesSerializer(favorites, many = True)
        
        try:
            obj = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            # return Response({'NotFound': 'User Queryset does not match.'})
            raise PermissionDenied

        if not obj == self.request.user:
            raise PermissionDenied
        return Response(serializer.data)
    
    def post(self, request, format=None, *args, **kwargs):
        print(self.request.user)
        if not request.data['user'] == self.request.user.pk:
            raise PermissionDenied

        serializer = UserFavoritesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class APIFavoritesUpdate(APIView):
    def get(self, request, format = None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        self.check_permission(self.request.user, user)
        favorite = self.get_object(user, kwargs['title'])
        serializer = UserFavoritesSerializer(favorite)
        return Response(serializer.data)
    
    def get_user(self, user_pk, *args, **kwargs):
        try:
            return User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise PermissionDenied

    def get_object(self, user_pk, favorite_title, *args, **kwargs):
        try:
            return Favorites.objects.filter(user = user_pk).filter(title = favorite_title)[0]
        except IndexError:
            raise NotFound
    
    def check_permission(self, request_user, user):
        # Permission check
        if not user == request_user:
            raise PermissionDenied

    def put(self, request, format=None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
    
        self.check_permission(request.data['user'], user.pk)
        favorite = self.get_object(user, kwargs['title'])
        serializer = UserFavoritesSerializer(favorite, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        self.check_permission(self.request.user.pk, user.pk)
        favorite = self.get_object(user, kwargs['title'])
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class APIRetrieveUpdateUserProfileDriver(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = UserProfileDriverMainSerializer
    permission_classes = (UserNestedProfilePermission,)
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserProfilePassenger(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = UserProfilePassengerMainSerializer
    permission_classes = (UserNestedProfilePermission,)
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserProfileTransmit(generics.RetrieveUpdateAPIView):
    queryset = Transmit.objects.all()
    serializer_class = UserProfileTransmitMainSerializer
    permission_classes = (UserNestedProfilePermission,)
    lookup_field = 'profile'
    lookup_url_kwarg = 'profile'

class APIRetrieveUpdateUserMachine(generics.RetrieveUpdateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = (UserMachinePermission,)
    lookup_field = 'driver'
    lookup_url_kwarg = 'driver'

class APIRetrieveUpdateUserBank(generics.RetrieveUpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = (UserMachinePermission,)
    lookup_field = 'driver'
    lookup_url_kwarg = 'driver'

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = MachineFeaturesSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

class APINotification(APIView):
    permission_classes = (UserPermission,)
    
    def get(self, request, format = None, *args, **kwargs):
        user_pk = kwargs['user']
        notifications = Notifications.objects.filter(user = user_pk)
        serializer = UserNotificationsSerializer(notifications, many = True)

        try:
            obj = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            # return Response({'NotFound': 'User Queryset does not match.'})
            raise PermissionDenied

        if not obj == self.request.user:
            raise PermissionDenied
        return Response(serializer.data)
    
    def post(self, request, format=None, *args, **kwargs):
        if not request.data['user'] == self.request.user.pk:
            raise PermissionDenied

        serializer = UserNotificationsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APINotificationUpdate(APIView):
    def get(self, request, format = None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        self.check_permission(self.request.user, user)
        notification = self.get_object(user, kwargs['notif'])
        serializer = UserNotificationsSerializer(notification)
        return Response(serializer.data)
    
    def get_user(self, user_pk, *args, **kwargs):
        try:
            return User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise PermissionDenied

    def get_object(self, user_pk, notif_pk, *args, **kwargs):
        try:
            return Notifications.objects.get(pk = notif_pk)
        except Notifications.DoesNotExist:
            raise NotFound
    
    def check_permission(self, request_user, user):
        # Permission check
        if not user == request_user:
            raise PermissionDenied

    def put(self, request, format=None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        self.check_permission(request.data['user'], user.pk)
        notification = self.get_object(user, kwargs['notif']) 
        serializer = UserNotificationsSerializer(notification, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, *args, **kwargs):
        user = self.get_user(user_pk = kwargs['user'])
        self.check_permission(self.request.user.pk, user.pk)
        notification = self.get_object(user, kwargs['notif'])
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######################
######## Trip ########
######################

class APITripListCreate(APIView):
    permission_class = (NormalPermission,)

    def get(self, request, format = None, *args, **kwargs):
        trips = Trip.objects.all()
        serializer = TripMainSerializer(trips, many = True)
        return Response(serializer.data)

    
    def post(self, request, format = None, *args, **kwargs):
        serializer = TripMainSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APITripRetrieveUpdate(APIView):
    permission_class = (NormalPermission,)

    def get(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        serializer = TripMainSerializer(trip)
        return Response(serializer.data)
    
    def put(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        serializer = TripMainSerializer(trip, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, trip, *args, **kwargs):
        try:
            return Trip.objects.get(pk = trip)
        except Trip.DoesNotExist:
            raise NotFound
        
class APIAllTripsUser(APIView):
    permission_class = (NormalPermission,)
    
    def get(self, request, format = None, *args, **kwargs):
        seats = Seat.objects.filter(user = self.request.user)
        trips = [Trip.objects.get(trip = seat.trip) for seat in seats]
        serializer = TripMainSerializer(trips, many = True)
        return Response(serializer.data)

class APISeatsATrip(APIView):

    permission_class = (NormalPermission,)

    def get(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        seats = Seat.objects.filter(trip = trip)
        serializer = SeatSerializer(seats, many = True)
        return Response(serializer.data)

    
    def get_object(self, trip, *args, **kwargs):
        try:
            return Trip.objects.get(pk = trip)
        except Trip.DoesNotExist:
            raise NotFound
    
    def post(self, request, format = None, *args, **kwargs):
        serializer = SeatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class APISeatsATripUpdate(APIView):
    permission_class = (NormalPermission, )

    def get(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        seat = Seat.objects.filter(trip = trip, position = kwargs['pos'])[0]

        serializer = SeatSerializer(seat)

        return Response(serializer.data)

    def put(self, request, format = None, *args, **kwargs):
        trip = self.get_object(kwargs['pk'])
        seat = Seat.objects.filter(trip = trip, position = kwargs['pos'])[0]
        # print(seat)
        serializer = SeatSerializer(seat, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_object(self, trip, *args, **kwargs):
        try:
            return Trip.objects.get(pk = trip)
        except Trip.DoesNotExist:
            raise NotFound

# class APIDriverTripTickets(APIView):
#     def get(self, request, format = None, *args, **kwargs):
#         tickets = TicketEnvelope.objects.filter(trip = kwargs['trip'])
#         serializer = TicketSerializer(tickets, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, format = None, *args, **kwargs):
#         serializer = TicketSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class APIDriverTripTicketUpdate(APIView):

#     def get(self, request, format = None, *args, **kwargs):
#         ticket = self.get_object(kwargs['ticket_sku'], kwargs['trip'])

#         if ticket:
#             serializer = TicketSerializer(ticket)
#             return Response(serializer.data)
#         else:
#             raise NotFound('Envelope Not Found')
        
#     def put(self, request, format = None, *args, **kwargs):
#         ticket = self.get_object(kwargs['ticket_sku'], kwargs['trip'])
#         serializer = TicketSerializer(ticket, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
            
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def get_object(self, sku, trip):
#         tickets = TicketEnvelope.objects.filter(trip = trip)
#         envelope = None
        
#         for ticket in tickets:
#             if ticket.sku == sku:
#                 return ticket
        
# class APITicketMessages(APIView):

#     def get(self, request, format = None, *args, **kwargs):
#         ticket = TicketEnvelope.objects.filter(trip = kwargs['trip']).filter(sku = kwargs['ticket_sku'])[0]
#         messages = ticket.messages.all()

#         # messages = TicketLetter.objects.all()
#         serializer = TicketLetterSerializer(messages, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, format = None, *args, **kwargs):
#         serializer = TicketLetterSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)