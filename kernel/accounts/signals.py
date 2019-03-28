from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone

from .models import User
from users.models import GeneralProfile
from users.models import Driver
from users.models import Passenger
from users.models import Transmit
from users.submodels.detail import Machine
from users.submodels.detail import Bank

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):    

    if created:
        GeneralProfile.objects.create(user=instance)

        # other profiles
        Passenger.objects.create(profile=instance.profile)
        Transmit.objects.create(profile=instance.profile)

        # Driver info profile
        Driver.objects.create(profile=instance.profile)
        Machine.objects.create(driver = instance.profile.driver)
        Bank.objects.create(driver = instance.profile.driver)

    else:
        instance.profile.save()
        instance.profile.driver.save()
        instance.profile.driver.machine.save()
        instance.profile.driver.bank.save()
        instance.profile.passenger.save()
        instance.profile.transmit.save()
