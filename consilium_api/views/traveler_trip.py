from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Traveler_Trip, Traveler, Trip

class TravelerTripSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Traveler_Trip
        url = serializers.HyperlinkedIdentityField(
            view_name='traveler_trip',
            lookup_field='id'
        )
        fields = ('id', 'traveler', 'trip', 'created_trip')
        depth = 1

class TravelerTrips(ViewSet):

    def create(self, request):

        traveler = Traveler.objects.get(user_id=request.auth.user.id)

        new_traveler_trip = Traveler_Trip()
        new_traveler_trip.traveler_id = Traveler.objects.get(user_id=request.auth.user.id)
        new_traveler_trip.trip_id = request.data['trip_id']  

        new_traveler_trip.save()

        serializer = TravelerTripSerializer(new_traveler_trip, context={'request': request})
        return Response(serializer.data)  

    def list(self, request):

        traveler_trips = Traveler_Trip.objects.all()
        serializer = TravelerTripSerializer(
            traveler_trips, many=True, context={'request': request}
        )

        return Response(serializer.data)       