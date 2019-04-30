from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import FAQCategory
from .models import RulesCategory

# Create your views here.
class HomeView(TemplateView):
    template_name = 'dashboard/index.html'
    title = 'خانه'


class SupportView(TemplateView):
    template_name = 'dashboard/support.html'
    title = 'پشتیبانی'

# class SettingsView(TemplateView):
#     template_name = 'dashboard/settings.html'
#     title = 'تنظیمات'

class ResetPasswordView(TemplateView):
    template_name = 'dashboard/reset-password.html'
    title = 'تغییر رمز عبور'

class FavoriteRoutesView(TemplateView):
    template_name = 'dashboard/favorite-routes.html'
    title = 'مسیرهای منتخب'

class FavoritesView(TemplateView):
    template_name = 'dashboard/favorites.html'
    title = 'علاقه مندی های من'

class NotificationView(TemplateView):
    template_name = 'dashboard/notifications.html'
    title = 'اعلان ها'

class FAQView(ListView):
    template_name = 'dashboard/faq.html'
    model = FAQCategory
    context_object_name = 'question_category'
    title = 'پرسش های متداول'

class RulesView(ListView):
    template_name = 'dashboard/rules.html'
    model = RulesCategory
    context_object_name = 'rules_category'
    title = 'قوانین'

class PassengerHomeView(TemplateView):
    template_name = 'dashboard/passenger/index.html'
    title = 'همسفر'
    category = 'passenger'

class DriverHomeView(TemplateView):
    template_name = 'dashboard/driver/index.html'
    title = 'راننده'
    category = 'driver'

