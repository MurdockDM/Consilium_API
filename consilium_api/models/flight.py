from django.db import models
from .traveler import Traveler
from .trip import Trip

class Flight(models.Model):

    start_airport = models.CharField(max_length=20)
    destination_airport = models.CharField(max_length=20)
    arrival_time = models.DateTimeField()
    traveler = models.ForeignKey(Traveler, related_name='flights', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name='trips', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "flight"
        verbose_name_plural = "flights"


    def __str__(self):
        return '{self.start_airport} to {self.destination_airport}'   
