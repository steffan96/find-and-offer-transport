from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    city = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        pass