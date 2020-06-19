from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .user import UserSerializer
from .traveler import TravelerSerializer
from consilium_api.models import TravelerTrip, Traveler, Trip

class TravelerTripSerializer(serializers.HyperlinkedModelSerializer):
    traveler = TravelerSerializer(many=False)
    class Meta:
        model = TravelerTrip
        url = serializers.HyperlinkedIdentityField(
            view_name='traveler_trip',
            lookup_field='id'
        )
        fields = ('id', 'traveler', 'trip', 'created_trip', 'trip_id')
        depth = 2

class TravelerTrips(ViewSet):

    def create(self, request):

        traveler = Traveler.objects.get(user_id=request.auth.user.id)

        new_traveler_trip = TravelerTrip()
        new_traveler_trip.traveler_id = traveler.id
        new_traveler_trip.trip_id = request.data['trip_id'] 
        new_traveler_trip.created_trip = request.data['created_trip']
        new_traveler_trip.save()

        serializer = TravelerTripSerializer(new_traveler_trip, context={'request': request})
        return Response(serializer.data)  

    def list(self, request):

        yourtrips = self.request.query_params.get('yourtrips', None)

        if yourtrips is not None:
            traveler = Traveler.objects.get(user = self.request.user)
            traveler_trips = TravelerTrip.objects.filter(traveler_id = traveler, created_trip=True)
        else:
            traveler_trips = TravelerTrip.objects.all()

        serializer = TravelerTripSerializer(
            traveler_trips, many=True, context={'request': request}
        )

        return Response(serializer.data)       