from django.shortcuts import render
from .models import Room

# Create your views here.
# studybud1/base/views.py
# They are functions or classes
# When someone goes to a specific URL, they will be sent here. Any queries to the DB will be sent here.

rooms = [
    {"id": 1, "name": "Learn Python"},
    {"id": 2, "name": "Learn Django"},
    {"id": 3, "name": "Front End Developers"},
]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i
    context = {"room": room}
    return render(request, "base/room.html", context)