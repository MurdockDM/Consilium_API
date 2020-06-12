from django.db import models
# from .traveler_trip import Traveler_Trip

class Trip(models.Model):

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    # traveler = models.ManyToManyField('Traveler', through=Traveler_Trip)

    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "trips"


    def __str__(self):
        return '{self.city} trip'    