from pkg_resources import require
from rest_framework import serializers
from .models import Client, User, Event

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('uuid','title', 'user', 'id')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('title','start', 'end', 'id', 'user', 'description')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    clients = serializers.StringRelatedField(many=True, read_only=True)
    events = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'clients', 'id', 'events' )

        extra_kwargs = {'password': {
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user