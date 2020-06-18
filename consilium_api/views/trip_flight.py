from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import TripFlight
from .flight import FlightSerializer


class TripFlightSerializer(serializers.HyperlinkedModelSerializer):

    flight = FlightSerializer(many=False)
    
    class Meta:
        model = TripFlight
        url = serializers.HyperlinkedIdentityField(
            view_name='trip_flight',
            lookup_field='id'
        )
        fields = ('id', 'trip', 'flight')
        depth = 1


class TripFlights(ViewSet):

    def create(self, request):

        new_trip_flight = TripFlight()
        new_trip_flight.trip = request.data['trip']
        new_trip_flight.flight = request.data['flight']

        new_trip_flight.save()

        serializer = TripFlightSerializer(
            new_trip_flight, context={'request': request})

        return Response(serializer.data)

    def list(self, request):

        trip_flights = TripFlight.objects.all()

        serializer = TripFlightSerializer(
            trip_flights, many=True, context={'request': request})

        return Response(serializer.data)
