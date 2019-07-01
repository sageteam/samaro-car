from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from ticket.models import TicketEnvelope

class TicketEnvelopeSerializer(ModelSerializer):
    class Meta:
        model = TicketEnvelope
        fields = ('subject', 'priority', 'status', 'department', 'trip', 'passenger', 'driver')

