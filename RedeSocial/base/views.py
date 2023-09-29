from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    room = Room.objects.all()

    context = {"rooms":room}
    return render(request, "home.html", context)

def RoomPage(request, pk):
    room = Room.objects.get(id=pk)
    context={"room":room}
    return render(request, "room.html", context)