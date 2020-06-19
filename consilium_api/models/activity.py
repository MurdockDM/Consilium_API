from django.db import models
from django.db.models import F
from .trip import Trip
from .traveler import Traveler


class Activity(models.Model):

    name = models.CharField(max_length=900)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        ordering = (F('trip').asc(), ('city'))