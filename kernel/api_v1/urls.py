from django.urls import include
from django.urls import re_path

from . import views

app_name = 'apis'
urlpatterns = [
    re_path(r'^city$', views.APIListCreateCity.as_view(), name = 'api_cities'),
    re_path(r'^city/update/(?P<pk>\d+)/$', views.APIRetrieveUpdateDestroyCity.as_view(), name = 'api_city'),
    re_path(r'^region$', views.APIListCreateRegion.as_view(), name = 'api_regions'),
    re_path(r'^region/update/(?P<pk>\d+)/$', views.APIRetrieveUpdateDestroyRegion.as_view(), name = 'api_region'),
    re_path(r'^distance$', views.APIListCreateDistance.as_view(), name = 'api_distances'),
    re_path(r'^distance/update/(?P<slug>[\w-]+)/$', views.APIRetrieveUpdateDestroyDistance.as_view(), name = 'api_distance'),
    re_path(r'^trip$', views.APIListCreateTrip.as_view(), name = 'api_trips'),
]