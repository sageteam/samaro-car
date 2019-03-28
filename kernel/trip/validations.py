from django.core.exceptions import ValidationError
from .models import Region

def validate_region_subset_of_city(value):
    regions = Region.objects.filter(city = value)
    
    if value == instance.origin:
        raise ValidationError('Origin Region must be subset of origin City.')
    
    if not instance.destiantion_region.city == instance.destination:
        raise ValidationError('Destination Region must be subset of destination City.')
