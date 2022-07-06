from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions

from .models import Client
from .serializers import ClientSerializer

def ok_view(request):
    return HttpResponse("ok!")

def list_clients(request):
    clients = Client.objects.all().values()
    clients_list = list(clients)
    return JsonResponse(clients_list, safe=False)

def mock_login(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})

def mock_signup(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})

class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['user_string'] = request.user.username
        return super().post(request, *args, **kwargs)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientListProtected(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    permission_classes = [permissions.IsAuthenticated]
