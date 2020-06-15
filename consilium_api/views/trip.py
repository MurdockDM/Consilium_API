from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Trip



class TripSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Trip
        url = serializers.HyperlinkedIdentityField(
            view_name = 'trip',
            lookup_field = 'id'
        )
        fields = ('id', 'city', 'state', 'country', 'start_date', 'end_date')
        depth = 1

class Trips(ViewSet):

    def create(self, request):
        new_trip = Trip()
        new_trip.city = request.data['city']
        new_trip.state = request.data['state']
        new_trip.country = request.data['country']
        new_trip.start_date = request.data['start_date']
        new_trip.end_date = request.data['end_date']
        new_trip.save()
        

        serializer = TripSerializer(new_trip, context={'request':request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)        

    def update(self, request, pk=None):
        trip = Trip.objects.get(pk=pk)
        trip.city = request.data['city']
        trip.state = request.data['state']
        trip.country = request.data['country']
        trip.start_date = request.data['start_date']
        trip.end_date = request.data['end_date']
        trip.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk=None):
        try:
            trip = Trip.objects.get(pk=pk)
            trip.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Trip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)            
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    def list(self, request):

        trips = Trip.objects.all()

        serializer = TripSerializer(trips, many=True, context={'request': request})
        return Response(serializer.data)            