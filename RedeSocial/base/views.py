from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {}
    return render(request, "home.html", context)

def Room(request):
    context={}
    return render(request, "room.html", context)