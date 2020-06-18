from django.db import models
from django.db.models import F


class Trip(models.Model):

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    traveler_on_trip = models.ManyToManyField('Traveler' , through='TravelerTrip')
    # flight = models.ManyToManyField('Flight', through='TripFlight')
    # accommodation = models.ManyToManyField('Accommodation', through='TripAccommodation')
    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "trips"
        ordering = (F('start_date').asc(),)

    def __str__(self):
        return '{self.city} trip'    