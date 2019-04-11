from django.urls import include
from django.urls import re_path
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'region', views.RegionViewSet)
router.register(r'distance', views.DistanceViewSet)
router.register(r'feature', views.FeatureViewSet)
router.register(r'login', views.APILoginViewSet, base_name='login')

app_name = 'api_v1'
urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'^user/(?P<email>\w+@\w+.\w+)/$', views.APIDetailUser.as_view(), name = 'user-detail'),
    re_path(r'^user/profile/(?P<user>\d+)/$', views.APIRetrieveUpdateUserProfile.as_view(), name = 'user-profile'),
    re_path(r'^user/(?P<user>\d+)/setting/$', views.APIRetrieveUpdateUserSetting.as_view(), name = 'api_user_profile_setting'),
    re_path(r'^user/profile/(?P<profile>\d+)/driver/$', views.APIRetrieveUpdateUserProfileDriver.as_view(), name = 'api_user_profile_driver'),
    re_path(r'^user/profile/(?P<profile>\d+)/passenger/$', views.APIRetrieveUpdateUserProfileDriver.as_view(), name = 'api_user_profile_passenger'),
    re_path(r'^user/profile/(?P<profile>\d+)/transmit/$', views.APIRetrieveUpdateUserProfilePassenger.as_view(), name = 'api_user_profile_transmit'),
    re_path(r'^user/profile/(?P<driver>\d+)/machine/$', views.APIRetrieveUpdateUserMachine.as_view(), name = 'api_user_machine'),
    re_path(r'^user/profile/(?P<driver>\d+)/bank/$', views.APIRetrieveUpdateUserBank.as_view(), name = 'api_user_bank'),
    re_path(r'^user/(?P<user>\d+)/favorites/$', views.APIFavoites.as_view(), name = 'api_user_favorites'),
    re_path(r'^user/(?P<user>\d+)/favorites/(?P<title>(\w+\s?)+)/$', views.APIFavoritesUpdate.as_view(), name = 'user-favorite-detail'),
    re_path(r'^user/(?P<user>\d+)/notifications/$', views.APINotification.as_view(), name = 'user-notifs'),
    re_path(r'^user/(?P<user>\d+)/notifications/(?P<notif>\d+)/$', views.APINotificationUpdate.as_view(), name = 'user-notifs-detail'),
    re_path(r'^register/$', views.APIRegisterViewSet.as_view(), name = 'user-registeration'),
    re_path(r'trips/$', views.APITripListCreate.as_view(), name = 'trips'),
    re_path(r'trips/user/(?P<user>\d+)/$', views.APIAllTripsUser.as_view(), name = 'user-trips'),
    re_path(r'trips/(?P<pk>\d+)/$', views.APITripRetrieveUpdate.as_view(), name = 'trips'),
    re_path(r'trip/(?P<pk>\d+)/seats/$', views.APISeatsATrip.as_view(), name = 'trip-seats'),
    re_path(r'trip/(?P<pk>\d+)/seat/(?P<pos>\d+)/$', views.APISeatsATripUpdate.as_view(), name = 'trip-seats-detail'),
    re_path(r'trip/(?P<trip>\d+)/tickets/', views.APIDriverTripTickets.as_view(), name = 'trip-driver-tickets'),
    re_path(r'trip/(?P<trip>\d+)/ticket/(?P<ticket_sku>\d+\w+)$', views.APIDriverTripTicketUpdate.as_view(), name = 'trip-ticket-detail'),
    re_path(r'trip/(?P<trip>\d+)/ticket/(?P<ticket_sku>\d+\w+)/messages/$', views.APITicketMessages.as_view(), name = 'trip-ticket-messages'),
]