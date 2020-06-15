from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Accommodation

class AccommodationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Accommodation
        url = serializers.HyperlinkedIdentityField(
            view_name = 'accommodation',
            lookup_field = 'id'
        )

        fields = ('id', 'name', 'address', 'city', 'state', 'check_in_date', 'checkout_date', 'capacity', 'booked', 'room' )
        depth = 1

class Accommodations(ViewSet):

    def create(self, request):
        new_accommodation = Accommodation()
        new_accommodation.name = request.data['name']
        new_accommodation.address = request.data['address']
        new_accommodation.city = request.data['city']
        new_accommodation.state = request.data['state']
        new_accommodation.check_in_date = request.data['check_in_date']
        new_accommodation.checkout_date = request.data['checkout_date']
        new_accommodation.capacity = request.data['capacity']
        new_accommodation.booked = request.data['booked']
        new_accommodation.room = request.data['room']
        new_accommodation.trip = request.data['trip']
        new_accommodation.save()

        serializer = AccommodationSerializer(new_accommodation, context={'request': request})
        
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            accommodation = Accommodation.objects.get(pk=pk)
            serializer = AccommodationSerializer(accommodation, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        accommodation = Accommodation.objects.get(pk=pk)
        accommodation.name = request.data['name']
        accommodation.address = request.data['address']
        accommodation.city = request.data['city']
        accommodation.state = request.data['state']
        accommodation.check_in_date = request.data['check_in_date']
        accommodation.checkout_date = request.data['checkout_date']
        accommodation.capacity = request.data['capacity']
        accommodation.booked = request.data['booked']
        accommodation.room = request.data['room']
        accommodation.trip = request.data['trip']
        accommodation.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            accommodation = Accommodation.objects.get(pk=pk)
            accommodation.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Accommodation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NO_CONTENT)        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):

        accommodations = Accommodation.objects.all()

        serializer = AccommodationSerializer(accommodations, many=True, context={'request': request}) 
        return Response(serializer.data)   
        
        
        
        
                        
        
        
        
        
        