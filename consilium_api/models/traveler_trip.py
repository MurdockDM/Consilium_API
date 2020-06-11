from django.db import models
from .traveler import Traveler
from .trip import Trip


class Traveler_Trip(models.Model):

    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_trip = models.BooleanField()
    