from django.db import models
from users.models import CustomUser


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)
    duration = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)