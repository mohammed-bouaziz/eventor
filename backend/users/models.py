from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_images', null=True, blank=True) 
    is_pro = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)





