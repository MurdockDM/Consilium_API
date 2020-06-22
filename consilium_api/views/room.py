from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Room, Accommodation

class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        url = serializers.HyperlinkedIdentityField(
            view_name = 'room',
            lookup_field = 'id'
        )
        fields = ('id', 'room_number')


class Rooms(ViewSet):

    def create(self, request):
        new_room = Room()
        new_room.room_number = request.data['room_number']
        new_room.save()


        serializer = RoomSerializer(new_room, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            room = Room.objects.get(pk=pk)
            serializer = RoomSerializer(room, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        room = Room.objects.get(pk=pk)
        room.room_number = request.data['room_number']
        room.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk=None):
        try:
            room = Room.objects.get(pk=pk)
            room.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Room.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        rooms = Room.objects.all()

        serializer = RoomSerializer(rooms, many=True, context={'request': request}) 
        return Response(serializer.data)                                          
