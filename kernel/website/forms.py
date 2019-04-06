from django import forms

import re

from django.forms import TextInput
from .models import PreRegisterDriver


class PreRegisterDriverForm(forms.ModelForm):
    """Form definition for PreRegisterDriver."""

    name = forms.CharField(label = 'نام', max_length = 128, required = True)
    last_name = forms.CharField(label = 'نام خانوادگی', max_length = 128, required = True)
    email = forms.CharField(label = 'ایمیل', max_length = 128, required = True)
    phone_number = forms.CharField(label = 'موبایل', max_length = 128, required = True)
    origin = forms.CharField(label = 'مبدا', max_length = 128, required = True)
    destination = forms.CharField(label = 'مقصد', max_length = 128, required = True)
    # national_code = forms.CharField(label = 'کد ملی', max_length = 128, required = True)


    error_messages = {
            'duplicate_email': ("ایمیل تکراری است. لطفا ایمیل دیگری امتحان کنید."),
            'duplicate_phone_number': ("شماره تماس تکراری است. لطفا شماره دیگری امتحان کنید.")
    }

    EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    class Meta:
        """Meta definition for PreRegisterDriverform."""
        model = PreRegisterDriver
        fields = ('__all__')

        
    def clean_email(self):
        email = self.cleaned_data['email']

        if self.instance.email == email:
            return email
        
        if email and not re.match(self.EMAIL_REGEX, email):
            raise forms.ValidationError('ایمیل نامعتبر است')
        
        try:
            PreRegisterDriver._default_manager.get(email = email)
        except PreRegisterDriver.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email'
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if self.instance.phone_number == phone_number:
            return phone_number
        
        if len(phone_number) != 11:
            raise forms.ValidationError('شماره موبایل را به درستی وارد نمایید.')

        try:
            PreRegisterDriver._default_manager.get(phone_number = phone_number)
        except PreRegisterDriver.DoesNotExist:
            return phone_number
        raise forms.ValidationError(
            self.error_messages['duplicate_phone_number'],
            code='duplicate_phone_number'
        )

