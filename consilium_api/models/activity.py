from django.db import models
from .trip import Trip
from .traveler import Traveler


class Activity(models.Model):

    name = models.CharField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"