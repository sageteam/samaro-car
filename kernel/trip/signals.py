from trip.models import Distance
from trip.models import Seat, Trip

from rest_framework.serializers import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from rest_framework.exceptions import NotAcceptable

@receiver(pre_save, sender=Distance)
def distance_model_pre_save_receiver(sender, instance, *args, **kwargs):
    # validations
    if instance.city1 == instance.city2:
        raise ValidationError({'203': ['cities must be distinct.']})

    # calculate price
    if 0 < instance.distance <= 300:
        instance.price = instance.distance * 65
    else:
        instance.price = instance.distance * 45


@receiver(post_save, sender=Distance)
def distance_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        pass
    
    if instance.city1 == instance.city2:
        raise ValidationError({'203': ['cities must be distinct.']})

@receiver(post_save, sender=Trip)
def create_trip_post_save(sender, instance, created, *args, **kwargs):
    if created:
        # create 4 seats for each trip
        Seat.objects.create(trip = instance, position = 1, state = 1)
        Seat.objects.create(trip = instance, position = 2, state = 1)
        Seat.objects.create(trip = instance, position = 3, state = 1)
        Seat.objects.create(trip = instance, position = 4, state = 1)
    
 

@receiver(pre_save, sender=Trip)
def create_trip_pre_save(sender, instance, *args, **kwargs):
    # If is Post HTTP Method
    if not instance.pk:
        if Trip.objects.has_active_trip(instance.driver):
            raise NotAcceptable(detail = 'The driver has a active trip.')
    if instance.pk:
        trip = Trip.objects.get(pk = instance.pk)
        if not instance.driver == trip.driver:
            raise NotAcceptable(detail = 'You can\'t change the driver.')
 

@receiver(post_save, sender=Seat)
def edit_seat_post_save(sender, instance, created, *args, **kwargs):
    if not created:
        driver = instance.trip.driver
        passenger = instance.user


