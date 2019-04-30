from django import forms
from trip.models import Trip
from trip.models import City
from trip.models import Distance
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone as tz
from datetime import timedelta
from khayyam import JalaliDatetime as jd


class DriverTripForm(forms.ModelForm):
    start_time = forms.DateTimeField(initial = jd.now().strftime('%Y-%m-%d %H:%M:%S'), label = _('زمان و تاریخ حرکت'))
    passenger_capacity = forms.ChoiceField(choices = Trip.CAPACITIES, label = _('ظرفیت مسافر'), initial = 4)
    suggested_price = forms.CharField(max_length=100000)

    def __init__(self, *args, **kwargs):
        super(DriverTripForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
        self.fields['back_seat_price'].required = True
    
    class Meta:
        model = Trip
        fields = ('origin', 'destination', 'origin_region', 'destination_region', 'discount', 'gender', 'start_time', 'is_dispatcher', 'item_capacity', 'front_seat_price', 'back_seat_price', 'passenger_capacity', 'status', 'driver', 'type_creator', 'suggested_price')

        widgets = {
            "status": forms.HiddenInput(),
            "driver": forms.HiddenInput(),
            "type_creator": forms.HiddenInput(),
        }

        labels = {
            "origin": _('مبدا'),
            "destination": _('مقصد'),
            "origin_region": _('ناحیه مبدا'),
            "destination_region": _('ناحیه مقصد'),
            "discount": _('میزان تخفیف'),
            "gender": _('جنسیت سفر'),
            "start_time": _('تاریخ و زمان حرکت'),
            "front_seat_price": _('قیمت صندلی جلو'),
            "back_seat_price": _('قیمت صندلی عقب'),
            "passenger_capacity": _('ظرفیت مسافر'),
            "item_capacity": _('ظرفیت بار'),
            "is_dispatcher": _('امکان ارسال مرسوله'),
        }
    
    def clean(self, *args, **kwargs):

        origin = self.cleaned_data.get('origin')
        destination = self.cleaned_data.get('destination')
        front_price = self.cleaned_data.get('front_seat_price')
        back_price = self.cleaned_data.get('back_seat_price')
        passenger_cap = self.cleaned_data.get('passenger_capacity')
        

        price = self.cleaned_data.get('suggested_price')


        distance = Distance.objects.filter(url__contains = origin.name).filter(url__contains = destination.name)[0]

        if int(price) > distance.price or int(front_price) > distance.price or int(back_price) > distance.price:
            raise forms.ValidationError('قیمت فیلدهای صندلی جلو، صندلی عقب و قیمت پیشنهادی نمی تواند بیشتر از قیمت پیشنهاد داده شده باشد.')

        driver = self.cleaned_data.get('driver')
        if Trip.objects.has_active_trip(driver):
            raise forms.ValidationError('شما یک سفر فعال دارید.')

        if origin == destination:
            raise forms.ValidationError('مبدا و مقصد نمی توانند یکی باشند.')

        if not passenger_cap:
            raise forms.ValidationError('تعداد ظرفیت مسافرین را وارد نکرده اید.')

        if not front_price:
            if front_price == 0:
                cap = int(passenger_cap)
                if cap > 3:
                    raise forms.ValidationError('زمانی که صندلی جلو پر باشد، ظرفیت حداکثر تا سه نفر می تواند باشد.')
            else:
                raise forms.ValidationError('قیمت صندلی جلو را وارد نکرده اید')

        if not back_price:
            raise forms.ValidationError('قیمت صندلی عقب را وارد نکرده اید')

    def clean_origin_region(self, *args, **kwargs):
        if self.cleaned_data.get('origin_region') == 0:
            raise forms.ValidationError('شهری ابتدا انتخاب کنید')
        return self.cleaned_data.get('origin_region')

    def clean_destination_region(self, *args, **kwargs):
        if self.cleaned_data.get('destination_region') == 0:
            raise forms.ValidationError('شهری ابتدا انتخاب کنید')
        return self.cleaned_data.get('destination_region')

    def clean_start_time(self, *args, **kwargs):
        year, month, day = self.cleaned_data['start_time'].strftime('%Y-%m-%d').split('-')
        hours, minutes, seconds = self.cleaned_data['start_time'].strftime('%H:%M:%S').split(':')
        shamsi = jd(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))
        
        # import pdb; pdb.set_trace()
        four_hours_later = jd.now() + timedelta(hours = 4)
        result = four_hours_later - shamsi.now()
        threshold = result.total_seconds() / 3600
        if threshold < 4:
            raise forms.ValidationError('مدت انتظار هر سفر حداقل چهار ساعت است.')

        # return converted to miladi
        return shamsi.todatetime()

class PassengerTripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PassengerTripForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
        self.fields['driver'].required = False
        self.fields['item_capacity'].required = False
    
    class Meta:
        model = Trip
        fields = ('origin', 'destination', 'origin_region', 'destination_region', 'gender', 'start_time', 'is_dispatcher', 'item_capacity', 'status', 'driver', 'type_creator')
        widgets = {
            "status": forms.HiddenInput(),
            "driver": forms.HiddenInput(),
            "type_creator": forms.HiddenInput(),
        }

        labels = {
            "origin": _('مبدا'),
            "destination": _('مقصد'),
            "origin_region": _('ناحیه مبدا'),
            "destination_region": _('ناحیه مقصد'),
            "gender": _('جنسیت سفر'),
            "start_time": _('تاریخ و زمان حرکت'),
            "item_capacity": _('ظرفیت بار'),
            "is_dispatcher": _('بار همراه خود دارم'),
        }