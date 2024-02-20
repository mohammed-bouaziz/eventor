from django.db import models
from users.models import CustomUser
from locations.models import Locations
from services.models import Service
from .services import _get_duration


class Event(models.Model):
    TYPES_OF_EVENTS = [
        ('on_site', 'On-Site'),
        ('virtual', 'Virtual')
    ]
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    type_of_event = models.CharField(max_length=10, choices=TYPES_OF_EVENTS, default="on_site")
    location = models.CharField(max_length=256, blank=True, null=True)
    created_by= models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.duration = _get_duration(self.start_time, self.end_time)
        super(Event, self).save(*args, **kwargs)

class Session(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    booking_time = models.DateTimeField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)







    


