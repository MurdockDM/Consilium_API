from django.db import models
from .room import Room
from .trip import Trip

class Accommodation(models.Model):

    name = models.CharField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    check_in_date = models.DateField()
    checkout_date = models.DateField()
    capacity = models.IntegerField(null=True, blank=True)
    booked = models.BooleanField()
    room = models.ForeignKey(Room, on_delete=)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)