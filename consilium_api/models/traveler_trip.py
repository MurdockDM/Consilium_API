from django.db import models
from .traveler import Traveler
from .trip import Trip


class TravelerTrip(models.Model):

    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_trip = models.BooleanField()

    class Meta:
        verbose_name = 'traveler trip'
        verbose_name_plural = 'traveler trips'
