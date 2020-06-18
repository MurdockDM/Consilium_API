# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from consilium_api.models import TripAccommodation

# class TripAccommodationSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = TripAccommodation
#         url = serializers.HyperlinkedIdentityField(
#             view_name='trip_accommodation',
#             lookup_field='id'
#         )
#         fields = ('id', 'trip', 'accommodation')
#         depth = 1


# class TripAccommodations(ViewSet):

#     def create(self, request):

#         new_trip_accommodation = TripAccommodation()
#         new_trip_accommodation.trip = request.data["trip"]
#         new_trip_accommodation.accommodation = request.data["accommodation"]
        

#         new_trip_accommodation.save()
        
#         serializer = TripAccommodationSerializer(new_trip_accommodation, context={'request': request})
#         return Response(serializer.data)

#     def list(self, request):

#         trip_accommodations = TripAccommodation.objects.all()

#         serializer = TripAccommodationSerializer(trip_accommodations, many=True, context={'request':request})
        
#         return Response(serializer.data)
                