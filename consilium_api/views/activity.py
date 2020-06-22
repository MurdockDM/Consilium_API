from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Activity, Traveler, Activity
from .traveler import TravelerSerializer


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    """Takes related fields from models and translates between JSON format and database. """
    
    traveler = TravelerSerializer(many=False)
    class Meta:
        model = Activity
        url = serializers.HyperlinkedIdentityField(
            view_name='activity',
            lookup_field='id'
        )
        fields = ('id', 'name', 'address', 'city', 'state', 'trip', 'traveler', 'trip_id', 'traveler_id')
        depth = 1


class Activities(ViewSet):
    """Methods used to act upon database for Activity database table. """
    def create(self, request):
        new_activity = Activity()
        traveler = Traveler.objects.get(user_id=request.auth.user.id)
        new_activity.name = request.data['name']
        new_activity.address = request.data['address']
        new_activity.city = request.data['city']
        new_activity.state = request.data['state']
        new_activity.trip_id = request.data['trip_id']
        new_activity.traveler_id = traveler.id
        new_activity.save()

        serializer = ActivitySerializer(new_activity, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            activity = Activity.objects.get(pk=pk)
            serializer = ActivitySerializer(
                activity, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        traveler = Traveler.objects.get(user_id=request.auth.user.id)
        activity = Activity.objects.get(pk=pk)
        activity.name = request.data['name']
        activity.address = request.data['address']
        activity.city = request.data['city']
        activity.state = request.data['state']
        activity.trip_id = request.data['trip_id']
        activity.traveler_id = traveler.id
        activity.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            activity = Activity.objects.get(pk=pk)
            activity.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Activity.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        youractivities = self.request.query_params.get('youractivities', None)

        if youractivities is not None:
            selftraveler = Traveler.objects.get(user = self.request.user)
            activities = Activity.objects.filter(traveler = selftraveler,)
        else:    
            activities = Activity.objects.all()

        serializer = ActivitySerializer(
            activities, many=True, context={'request': request})
        return Response(serializer.data)
