from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

admin.site.register(Room)  # register the model with django
admin.site.register(Topic) # register the model with django
admin.site.register(Message) # register the model with django