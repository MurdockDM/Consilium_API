from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Flight, Traveler
from .traveler import TravelerSerializer
from .trip import TripSerializer

class FlightSerializer(serializers.HyperlinkedModelSerializer):

    traveler = TravelerSerializer(many=False)
    
    class Meta:
        model = Flight
        url = serializers.HyperlinkedIdentityField(
            view_name='flight',
            lookup_field='id'
        )
        fields = ('id', 'start_airport', 'destination_airport', 'arrival_time', 'traveler', 'trip', 'trip_id', 'traveler_id')
        depth = 1

class Flights(ViewSet):

    def create(self, request):
        traveler = Traveler.objects.get(user_id=request.auth.user.id)

        new_flight = Flight()
        new_flight.start_airport = request.data['start_airport']
        new_flight.destination_airport = request.data['destination_airport']
        new_flight.arrival_time = request.data['arrival_time']
        new_flight.traveler_id = traveler.id
        new_flight.trip_id = request.data['trip_id']
        new_flight.save()

        serializer = FlightSerializer(new_flight, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            flight = Flight.objects.get(pk=pk)
            serializer = FlightSerializer(flight, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        traveler = Traveler.objects.get(user_id=request.auth.user.id)
        flight = Flight.objects.get(pk=pk)
        flight.start_airport = request.data['start_airport']
        flight.destination_airport = request.data['destination_airport']
        flight.arrival_time = request.data['arrival_time']
        flight.traveler_id = traveler.id
        flight.trip_id = request.data['trip_id']
        flight.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            flight = Flight.objects.get(pk=pk)
            flight.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Flight.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)            
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       

    def list(self, request):

        yourflights = self.request.query_params.get('yourflights', None)

        if yourflights is not None:
            user = self.request.user
            traveler = Traveler.objects.get(user_id=user.id)
            flights = Flight.objects.filter(traveler_id=traveler.id)
        else:
            flights = Flight.objects.all()

        serializer = FlightSerializer(flights, many=True, context={'request': request})
        return Response(serializer.data)
