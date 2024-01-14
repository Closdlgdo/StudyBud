from django.shortcuts import render

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
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request):
    return render(request, "base/room.html")