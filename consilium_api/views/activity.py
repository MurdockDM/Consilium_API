from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Activity


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        url = serializers.HyperlinkedIdentityField(
            view_name = 'activity',
            lookup_field = 'id'
        )
        fields = ('id', 'name', 'address', 'city', 'state', 'trip', 'traveler')
        depth = 1

class Activities(ViewSet):

    def create(self, request):
        new_activity = Activity()
        new_activity.name = request.data['name']
        new_activity.address = request.data['address']
        new_activity.city = request.data['city']
        new_activity.state = request.data['state']
        new_activity.trip = request.data['trip']
        new_activity.traveler = request.data['traveler']
        new_activity.save()

        serializer = Activities(new_activity, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            activity = Activity.objects.get(pk=pk)
            serializer = ActivitySerializer(activity, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        activity = Activity.objects.get(pk=pk)
        activity.name = request.data['name']
        activity.address = request.data['address']
        activity.city = request.data['city']
        activity.state = request.data['state']
        activity.trip = request.data['trip']
        activity.traveler = request.data['traveler']
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

        activities = Activity.objects.all()

        serializer = ActivitySerializer(activities, many=True, context={'request': request})
        return Response(serializer.data)    
                        
        
        
        
                