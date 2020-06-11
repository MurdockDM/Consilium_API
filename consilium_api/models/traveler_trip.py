from django.db import models
from django.contrib.auth.models import User


class Traveler(models.Model):

    user = models.OneToOneField(User, related_name='traveler', on_delete=models.CASCADE)
    home_city = models.CharField(max_length=75)
    home_state = models.CharField(max_length=75)
    