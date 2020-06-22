from django.db import models
from django.db.models import F
from .room import Room
from .trip import Trip

class Accommodation(models.Model):

    name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    checkin_date = models.DateField(null=True, blank=True)
    checkout_date = models.DateField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    booked = models.BooleanField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        ordering = (F('trip').asc(), ('checkin_date'))