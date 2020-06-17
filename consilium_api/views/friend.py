from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from consilium_api.models import Friend, Traveler

class FriendSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Friend
        url = serializers.HyperlinkedIdentityField(
            view_name='friend',
            lookup_field='id'
        )
        fields = ('id', 'current_user', 'friend_user', 'request_accepted', )
        depth = 1

class Friends(ViewSet):

    def create(self, request):

        new_friend = Friend()
        new_friend.current_user = Traveler.objects.get(user_id=request.auth.user.id)
        new_friend.friend_user = request.data['friend_user']

        serializer = FriendSerializer(new_friend, context={'request': request})
        return Response(serializer.data)

    def list(self, request):
        user = self.request.user
        friends = Friend.objects.filter(current_user=user, request_accepted=True)
        serializer = FriendSerializer(
            friends, many=True, context={'request': request})

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            friend = Friend.objects.get(pk=pk)
            friend.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Friend.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

