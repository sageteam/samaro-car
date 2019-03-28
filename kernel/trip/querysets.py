from django.db.models import query
from django.db.models import Manager

class TripModelQuerySet(query.QuerySet):
    def driver_pending_trips(self, value):
        PENDING = 1
        return self.filter(driver = value).filter(status = PENDING)
    
    def active(self):
        return self.filter(active = True)
    

class TripModelManager(Manager):
    def get_queryset(self):
        return TripModelQuerySet(self.model, using=self._db)
    
    def has_active_trip(self, value):
        result = self.get_queryset().driver_pending_trips(value)
        return True if any(result) else False

    def all(self, *args, **kwargs):
        # All active trips trips
        return self.get_queryset().active()
