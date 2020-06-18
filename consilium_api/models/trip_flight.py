# from django.db import models
# from django.db.models import F
# from .trip import Trip
# from .flight import Flight

# class TripFlight(models.Model):

#     trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

#     class Meta:
#         ordering = (F('trip_id').asc(),)
