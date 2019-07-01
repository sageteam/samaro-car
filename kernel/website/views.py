from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import PreRegisterDriver
from .forms import PreRegisterDriverForm


class HomeView(TemplateView):
    template_name = 'index.html'
    title = 'خانه'

class PreRegister(CreateView):
    template_name = "others/pre-register.html"
    model = PreRegisterDriver
    form_class = PreRegisterDriverForm
    success_url = reverse_lazy('samaro:success')
    title = 'پیش ثبت نام'


class SuccessPage(TemplateView):
    template_name = 'others/success.html'
    title = 'سمارو | پیش ثبت نام'



