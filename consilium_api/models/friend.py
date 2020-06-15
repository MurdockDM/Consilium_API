from django.db import models
from .traveler import Traveler

class Friend(models.Model):

    current_user = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    friend_user = models.ForeignKey(Traveler, related_name='friends', on_delete=models.CASCADE)
    request_accepted = models.BooleanField()


    class Meta:
        verbose_name = 'friend'
        verbose_name_plural = 'friends'