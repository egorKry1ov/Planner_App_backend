from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions, viewsets

from .models import Client, User, Event
from .serializers import ClientSerializer, UserSerializer, EventSerializer

class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
     return Client.objects.all().filter(user_id=self.request.user)

    def post(self, request, *args, **kwargs):
        user_url = f'https://appoitment-planner-api.herokuapp.com/api/users/{request.user.id}/'
        request.data['user'] = user_url        
        return super().post(request, *args, **kwargs)

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
     return Event.objects.all().filter(user_id=self.request.user)

    def post(self, request, *args, **kwargs):
        user_url = f'https://appoitment-planner-api.herokuapp.com/api/users/{request.user.id}/'
        request.data['user'] = user_url        
        return super().post(request, *args, **kwargs)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class ClientListProtected(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
