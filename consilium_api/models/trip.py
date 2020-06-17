from django.db import models
from .traveler import Traveler

class Trip(models.Model):

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    traveler_on_trip = models.ManyToManyField('Traveler' , through='TravelerTrip')

    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "trips"


    def __str__(self):
        return '{self.city} trip'    