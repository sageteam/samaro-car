import secrets 
import khayyam
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import TicketLetter
from .models import TicketEnvelope

@receiver(pre_save, sender=TicketLetter)
def create_ticket_letter_pre_save(sender, instance, *args, **kwargs):
    passenger = instance.reply.passenger
    driver = instance.reply.driver

    if instance.user == passenger or instance.user == driver:
        pass
    else:
        raise Exception('The user has not permission to enter this ticket.')
    
    END = 2
    if instance.reply.trip.status == END:
        raise Exception('Trip is Ended. We can\'t send your message')
    
    
    instance.sku = secrets.token_hex(3)


@receiver(pre_save, sender=TicketEnvelope)
def create_ticket_envelope_pre_save(sender, instance, *args, **kwargs):
    END = 2
    if instance.trip.status == END:
        raise Exception('Trip is Ended. We can\'t send your message')
    
    today = khayyam.JalaliDatetime.now().strftime('%y%m%d')
    security_code = secrets.token_hex(3)
    instance.sku = '{}{}'.format(today, security_code)


@receiver(post_save, sender=TicketEnvelope)
def create_ticket_envelope_post_save(sender, instance, created, *args, **kwargs):
    # Send Email each time TicketEnvelope created
    # Send Email to driver
    # Send Email to passenger
    pass