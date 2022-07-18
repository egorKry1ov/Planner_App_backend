from django.urls import path, include
from . import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
 
    path('api/', include(router.urls)),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>', views.ClientDetail.as_view()),

    path('clients_protected/', views.ClientListProtected.as_view())
]