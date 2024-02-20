from django.db import models
from users.models import CustomUser

class Locations(models.Model):
    name = models.CharField(max_length=128)
    adresse = models.CharField(max_length=128, null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)


