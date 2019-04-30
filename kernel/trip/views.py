from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic import ListView
from trip.forms import DriverTripForm
from trip.forms import PassengerTripForm
from trip.models import Trip
from trip.models import Distance
from trip.models import City
from trip.models import Seat
from django.contrib import messages


# Create your views here.
class DriverTripCreateView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        form = DriverTripForm()
        
        return render(self.request, "dashboard/driver/driver-trip-submit.html", context={'form': form, 'category': 'driver'})
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.POST.copy()
            data['status'] = '1'
            data['driver'] = str(self.request.user.profile.driver.pk)
            data['type_creator'] = 1
            price = int(data['suggested_price'])

            # origin = City.objects.get(pk = int(data['origin']))
            # destination = City.objects.get(pk = int(data['destination']))
            # distance = Distance.objects.filter(url__contains = origin).filter(url__contains = destination)[0]

            
            
            form = DriverTripForm(data)
            if form.is_valid():
                form.save()
                price = int(data['front_seat_price'])
                if price == 0:
                    cap = int(data['passenger_capacity'])
                    import pdb; pdb.set_trace()
                    driver_id = self.request.user.profile.driver.pk
                    trip = Trip.objects.filter(driver = driver_id).filter(active = True).filter(status = 1)[0]
                    pos = 2
                    for capacity in range(1, cap + 1):
                        if not int(data['front_seat_price']) == 0:
                            Seat.objects.create(trip = trip, position = 1, state = 1)
                        Seat.objects.create(trip = trip, position = pos, state = 1)
                        pos += 1
            else:
                return render(self.request, "dashboard/driver/driver-trip-submit.html", context={'form': form, 'category': 'driver', 'title': 'ساخت سفر'})
        except KeyError:
            messages.add_message(request, messages.ERROR, 'خطا در هنگام ثبت رخ داده است.')
            messages.add_message(request, messages.INFO, 'لطفا فرم را با دقت پر نمایید.')
            return render(self.request, "dashboard/driver/driver-trip-submit.html", context={'form': form, 'category': 'driver', 'title': 'ساخت سفر'})

        return redirect('driver-trip')

class DriverActiveTrip(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/driver/driver-trip-list.html'
    context_object_name = 'active_trips'
    category = 'driver'
    title = 'سفرهای کنونی'

    def get_queryset(self):
        return Trip.objects.get_active_trips(self.request.user.profile.driver.pk)

class DriverPreviousTrip(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/driver/driver-trip-previous.html'
    context_object_name = 'previous_trips'
    category = 'driver'
    title = 'سفرهای پیشین'

    def get_queryset(self):
        return Trip.objects.get_previous_trips(self.request.user.profile.driver.pk)

class DriverAbortTrip(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/driver/driver-trip-aborted.html'
    context_object_name = 'aborted_trips'
    category = 'driver'
    title = 'سفرهای لغو شده'

    def get_queryset(self):
        return Trip.objects.get_aborted_trips(self.request.user.profile.driver.pk)

class DriverTripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/driver/driver-trips.html'
    context_object_name = 'trips'
    category = 'driver'
    
    def get_queryset(self):
        return Trip.objects.get_trips(2)

class PassengerTripCreateView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        form = PassengerTripForm()
        
        return render(self.request, "dashboard/passenger/passenger-trip-submit.html", context={'form': form, 'category': 'passenger'})
    
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['status'] = 1
        data['driver'] = None
        data['type_creator'] = 2
        
        form = PassengerTripForm(data)
        
        if form.is_valid():
            form.save()
        else:
            return render(self.request, "dashboard/passenger/passenger-trip-submit.html", context={'form': form, 'category': 'passenger'})
        
        return redirect('passenger-trip')

class PassengerActiveTrip(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/passenger/passenger-trip-list.html'
    context_object_name = 'active_trips'
    category = 'passenger'
    title = 'سفر های فعال'

    def get_queryset(self):
        return Trip.objects.get_active_trips_passenger(self.request.user.profile.driver.pk)

class PassengerPreviousTrip(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/passenger/passenger-trip-previous.html'
    context_object_name = 'previous_trips'
    category = 'passenger'
    title = 'سفرهای پیشین'

    def get_queryset(self):
        return Trip.objects.get_previous_trips_passenger(self.request.user.profile.driver.pk)

class PassengerAbortTrip(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/passenger/passenger-trip-aborted.html'
    context_object_name = 'aborted_trips'
    category = 'passenger'
    title = 'سفرهای لغو شده'

    def get_queryset(self):
        return Trip.objects.get_aborted_trips_passenger(self.request.user.profile.driver.pk)

class PassengerTripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'dashboard/passenger/passenger-trips.html'
    context_object_name = 'trips'
    category = 'passenger'
    title = 'لیست سفرها'
    
    def get_queryset(self):
        return Trip.objects.get_trips(1)
    
    def get_context_data(self, *args, **kwargs):
        qs = super(PassengerTripListView, self).get_queryset(*args, **kwargs)
        import pdb; pdb.set_trace()
        context = super(PassengerTripListView, self).get_context_data(**kwargs)
        # context['across'] = 

        return context
