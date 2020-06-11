from django.db import models


class Room(models.Model):

    room_number = models.CharField(max_length=20)


    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"
        


    def __str__(self):
        return self.room_number    