from trip.models import Distance
from trip.models import Seat, Trip

from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Distance)
def distance_model_pre_save_receiver(sender, instance, *args, **kwargs):
    # import pdb; pdb.set_trace()
    if not instance.url and instance.city1 and instance.city2:
        instance.url = slugify('{} {}'.format(instance.city1, instance.city2))
    
    if 0 < instance.distance <= 300:
        instance.price = instance.distance * 65
    else:
        instance.price = instance.distance * 45

@receiver(post_save, sender=Distance)
def distance_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.url and instance.city1 and instance.city2:
            instance.url = slugify('{} {}'.format(instance.city1, instance.city2))
            if 0 < instance.distance <= 300:
                instance.price = instance.distance * 65
            else:
                instance.price = instance.distance * 45
            
            instance.save()

@receiver(post_save, sender=Trip)
def create_trip_post_save(sender, instance, created, *args, **kwargs):
    if created:
        # create 4 seats for each trip
        Seat.objects.create(trip = instance, position = 1, state = 1)
        Seat.objects.create(trip = instance, position = 2, state = 1)
        Seat.objects.create(trip = instance, position = 3, state = 1)
        Seat.objects.create(trip = instance, position = 4, state = 1)

    else:
        instance.seat.save()

@receiver(pre_save, sender=Trip)
def create_trip_pre_save(sender, instance, *args, **kwargs):
    if Trip.objects.has_active_trip(instance.driver):
        raise ValueError('The driver has a active trip.')
    
    
@receiver(post_save, sender=Seat)
def edit_seat_post_save(sender, instance, created, *args, **kwargs):
    if not created:
        driver = instance.trip.driver
        passenger = instance.user


