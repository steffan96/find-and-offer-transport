from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.dispatch import receiver # Import the receiver
from .models import CustomUser

