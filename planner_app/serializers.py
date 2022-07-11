from pkg_resources import require
from rest_framework import serializers
from .models import Client, User

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('uuid','name', 'user', 'id')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    clients = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'clients', 'id' )

        extra_kwargs = {'password': {
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user