from django.db import models
from events.models import Event, Session

class EventInvitation(models.Model):
    STATUS = [
        ('pending', 'Pending'), 
        ('accepted', 'Accepted'), 
        ('declined', 'Declined')
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')

class SessionInvitation(models.Model):
    STATUS = [
        ('scheduled', 'Scheduled'), 
        ('canceled', 'Canceled'), 
        ('completed', 'Completed')
    ]
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='scheduled')
