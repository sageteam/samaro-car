from django.contrib import admin
from .models import PreRegisterDriver

# Register your models here.

@admin.register(PreRegisterDriver)
class PreRegisterDriverAdmin(admin.ModelAdmin):
    '''Admin View for PreRegisterDriver'''

    list_display = ('name', 'last_name', 'email', 'phone_number', 'origin', 'destination', 'created')
    ordering = ('-created',)
