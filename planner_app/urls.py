from django.urls import path
from . import views

urlpatterns = [
    
    path('ok/', views.ok_view),
    path('list_clients', views.list_clients),

    path('mock_login', views.mock_login),
    path('mock_signup', views.mock_signup),

    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>', views.ClientDetail.as_view()),

    path('clients_protected/', views.ClientListProtected.as_view())
]