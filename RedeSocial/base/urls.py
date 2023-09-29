from django.urls import path
from .views import *

urlpatterns = [
    path('', Home,  name="home"),
    path('room/<str:pk>',RoomPage, name="room"),
    path("login/", LoginPage, name="login"),
    path("logout/", Lougout, name="logout"),
    path("register/", RegisterPage, name="register"),
    path("create/", CreateRoom, name="create")
]