from django.db import models
from django.contrib.auth.models import User
# from .traveler_trip import Traveler_Trip

class Traveler(models.Model):

    user = models.OneToOneField(User, related_name='traveler', on_delete=models.CASCADE)
    home_city = models.CharField(max_length=75)
    home_state = models.CharField(max_length=75)
    # trip = models.ManyToManyField('Trip', through=Traveler_Trip)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'