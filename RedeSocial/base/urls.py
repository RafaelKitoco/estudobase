from django.urls import path
from .views import *

urlpatterns = [
    path('', Home,  name="home"),
    path('room/<str:pk>',RoomPage, name="room"),

]