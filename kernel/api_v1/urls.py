from django.urls import include
from django.urls import re_path

from . import views

app_name = 'apis'
urlpatterns = [
    re_path(r'^city$', views.APIListCreateCity.as_view(), name = 'api_city'),
    re_path(r'^city/detail$', views.APIDetailCity.as_view(), name = 'api_city_detail'),
    re_path(r'^city/(?P<name>[\w|\W]+)/$', views.APIRetrieveUpdateCity.as_view(), name = 'api_city'),

    re_path(r'^region$', views.APIListCreateRegion.as_view(), name = 'api_regions'),
    re_path(r'^region/(?P<name>[\w|\W]+)/$', views.APIRetrieveUpdateRegion.as_view(), name = 'api_region'),
    
    re_path(r'^distance$', views.APIListCreateDistance.as_view(), name = 'api_distances'),
    re_path(r'^distance/detail/$', views.APIDetailDistance.as_view(), name = 'api_distance_detail'),
    re_path(r'^distance/(?P<url>[\w-]+)/$', views.APIRetrieveUpdateDistance.as_view(), name = 'api_distance'),

    re_path(r'^trip/$', views.APIListCreateTrip.as_view(), name = 'api_trips'),
    re_path(r'^trip/(?P<pk>\d+)/$', views.APIListCreateTrip.as_view(), name = 'api_trip'),
    re_path(r'^trip/detail/(?P<pk>\d+)/$', views.APIListTrip.as_view(), name = 'api_trip_detail'),

    re_path(r'^user/$', views.APIListCreateUser.as_view(), name = 'api_user'),
    re_path(r'^user/detail/(?P<email>\w+@\w+.\w+)/$', views.APIDetailUser.as_view(), name = 'api_user_detail'),
    re_path(r'^user/profile/(?P<user>\d+)/$', views.APIRetrieveUpdateUserProfile.as_view(), name = 'api_user_profile'),
    re_path(r'^user/profile/(?P<profile>\d+)/driver/$', views.APIRetrieveUpdateUserProfileDriver.as_view(), name = 'api_user_profile_driver'),
    re_path(r'^user/profile/(?P<profile>\d+)/passenger/$', views.APIRetrieveUpdateUserProfilePassenger.as_view(), name = 'api_user_profile_passenger'),
    re_path(r'^user/profile/(?P<profile>\d+)/transmit/$', views.APIRetrieveUpdateUserProfileTransmit.as_view(), name = 'api_user_profile_transmit'),
    re_path(r'^user/(?P<email>\w+@\w+.\w+)/$', views.APIRetrieveUpdateUser.as_view(), name = 'api_user_update'),
]