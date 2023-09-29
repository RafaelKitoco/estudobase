from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from .form import *

# Create your views here.
def Home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    room = Room.objects.filter(Q(name__contains=q) | Q(topics__name__contains=q) | Q(desc__contains=q))
    topics = Topics.objects.all()
    count = room.count()

    context = {"rooms":room, "topics":topics, "count":count}
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
        password = request.POST.get("password")
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
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {"form":form}
    return render(request, "register_room.html", context)