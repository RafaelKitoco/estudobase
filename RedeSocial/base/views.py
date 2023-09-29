from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def Home(request):
    room = Room.objects.all()

    context = {"rooms":room}
    return render(request, "home.html", context)

def RoomPage(request, pk):
    room = Room.objects.get(id=pk)
    context={"room":room}
    return render(request, "room.html", context)

def LoginPage(request):
    page = "login"
    context = {"page":page}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POS.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "ERRO USUARIO NAO EXISTENTE")
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "nome do usuario ou palavra passe inexitente !")

    return render(request, "login.html", context)

def Lougout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
    
    return redirect("home")

def RegisterPage(request):
    page = "register"
    room_create = UserCreationForm()
    
    if request.method == "POST":
        room = UserCreationForm(request.POST)
        user = room.save(commit=False)
        user.username = user.username.lower()
        if room.is_valid():
            room.save()
            login(request, user)
            return redirect("home")
    context = {"form":room_create}
    return render(request, "login.html", context)

def CreateRoom(request):
    context = {}
    return render(request, "registe_room.html", context)