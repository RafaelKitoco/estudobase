from django.urls import path
from .views import *

urlpatterns = [
    path('', Home,  name="home"),
    path('room/<str:pk>',RoomPage, name="room"),
    path("login/", LoginPage, name="login"),
    path("logout/", Lougout, name="logout"),
    path("register/", RegisterPage, name="register"),
    path("create/", CreateRoom, name="create"),
    path("update/<str:pk>", UpdatePage, name="update"),
    path("delete/<str:pk>", DeletePage, name="delete"),
    path("delete-mensage/<str:pk>", DeleteMensage, name="delete-mensage"),
    path("update-mensage/<str:pk>", UpdateMensage, name="update-mensage")
]