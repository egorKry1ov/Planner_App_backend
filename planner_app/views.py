from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions, viewsets

from .models import Client, User
from .serializers import ClientSerializer, UserSerializer

def ok_view(request):
    return HttpResponse("ok!")

def list_clients(request):
    clients = Client.objects.all().values()
    clients_list = list(clients)
    return JsonResponse(clients_list, safe=False)



class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):

        # print(request.user.pk)
        # print(request.user.id)
        # output = User.objects.get(id=request.user.id)
        # print(output)

        user_url = f'http://127.0.0.1:8000/api/users/{request.user.id}/'

        request.data['user'] = user_url        

        return super().post(request, *args, **kwargs)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientListProtected(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
