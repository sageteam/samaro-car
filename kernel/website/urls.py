from django.urls import include
from django.urls import path
from django.urls import re_path

from . import views


app_name = 'samaro'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
]


# Pre Register
urlpatterns += [
    # re_path(r'^success/$', views.SuccessPage.as_view(), name='success'),
    # re_path(r'^$', views.PreRegister.as_view(), name='pre-register'),
]
