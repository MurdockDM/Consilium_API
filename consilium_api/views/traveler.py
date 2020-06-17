from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .user import UserSerializer
from consilium_api.models import Traveler


class TravelerSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(many=False)
    class Meta:
        model = Traveler
        url = serializers.HyperlinkedIdentityField(
            view_name='traveler',
            lookup_field='id'
        )
        fields = ('id', 'home_city', 'home_state', 'user', 'trip_for_traveler', 'possible_friend')
        
        depth = 1
        


class Travelers(ViewSet):

    def list(self, request):



        travelers = Traveler.objects.all()

        serializer = TravelerSerializer(travelers, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):


        try:
            traveler = Traveler.objects.get(pk=pk)
            serializer = TravelerSerializer(traveler, context={'request':request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)        