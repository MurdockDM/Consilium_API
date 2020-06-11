from django.db import models


class Trip(models.Model):

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    

    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "trips"


    def __str__(self):
        return '{self.city} trip'    