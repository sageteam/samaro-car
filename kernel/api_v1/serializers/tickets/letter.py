from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SlugRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from ticket.models import TicketLetter

class TicketLetterSerializer(ModelSerializer):
    class Meta:
        model = TicketLetter
        fields = ('message', 'ticket', 'user', 'reply')