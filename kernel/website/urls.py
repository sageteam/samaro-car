from django.urls import include
from django.urls import path
from django.urls import re_path

from . import views


app_name = 'site'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^success/$', views.SuccessPage.as_view(), name='success'),
]
