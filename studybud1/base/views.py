from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# studybud1/base/views.py
# They are functions or classes
# When someone goes to a specific URL, they will be sent here. Any queries to the DB will be sent here.


def home(request):
    return render(request, "home.html")


def room(request):
    return render(request, "room.html")