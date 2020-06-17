from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .user import UserSerializer
from consilium_api.models import Trip, Friend, Traveler



class TripSerializer(serializers.HyperlinkedModelSerializer):

    
    class Meta:
        model = Trip
        url = serializers.HyperlinkedIdentityField(
            view_name = 'trip',
            lookup_field = 'id'
        )
        fields = ('id', 'city', 'state', 'country', 'start_date', 'end_date', 'traveler_on_trip')
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

        
        
        friendstrips = self.request.query_params.get('friendstrips', None)
        

        if friendstrips is not None:
            user = self.request.user
            traveler = Traveler.objects.get(user_id = user.id)
            friends = Friend.objects.filter(current_user=traveler, request_accepted=True)
            all_trips = Trip.objects.filter(traveler_on_trip__id__in = friends)
        else:
            all_trips = Trip.objects.all()    
        
        serializer = TripSerializer(all_trips, many=True, context={'request': request})
        return Response(serializer.data)            