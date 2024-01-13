from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# studybud1/base/views.py
# They are functions or classes
# When someone goes to a specific URL, they will be sent here. Any queries to the DB will be sent here.


def home(request):
    return HttpResponse("Home page")


def room(request):
    return HttpResponse("Room")