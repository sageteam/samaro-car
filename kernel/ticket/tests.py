from django.test import TestCase
from django.utils import timezone as tz

from ticket.models import TicketEnvelope, TicketLetter
from trip.models import Trip, Seat
from trip.models import City, Region
from accounts.models import User

class TicketEnvelopeModel(TestCase):
    def setUp(self):
        self.city1 = City.objects.create(name = 'Nowshahr')
        self.city2 = City.objects.create(name = 'Tehran')
        self.region1 = Region.objects.create(name = 'Homafaran', city = self.city1)
        self.region2 = Region.objects.create(name = 'TehranPars', city = self.city2)
        self.passenger = User.objects.create(email = 'passenger@gmail.com', password = 'sepehr1234')
        self.driver = User.objects.create(email = 'driver@gmail.com', password = 'sepehr1234')
        self.trip = Trip.objects.create(start_time = tz.now(), end_time = tz.now(), origin = self.city1, destination = self.city2, origin_region = self.region1, destination_region = self.region2, driver = self.driver, status = 1 )
        self.ticket = TicketEnvelope.objects.create(
            subject = 'this trip',
            trip = self.trip,
            passenger = self.passenger,
            driver = self.driver
        )

        self.message1 =  TicketLetter.objects.create(message = 'hello', user = self.passenger, reply = self.ticket)
        self.message2 =  TicketLetter.objects.create(message = 'hello', user = self.driver, reply = self.ticket)

    def test_raise_error_trip_is_ended(self):
        with self.assertRaises(Exception):
            self.trip.status = 2
            
            self.ticket2 = TicketEnvelope.objects.create(
                subject = 'this trip',
                trip = self.trip,
                passenger = self.passenger,
                driver = self.driver
            )
