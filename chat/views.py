from django.shortcuts import render
from .models import *

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    message = Message.objects.filter(chat_room=room_name)
    message_info = message.values_list('message', 'message_by__name')
    return render(request, "chat/room.html", {"room_name": room_name, 'messages': message_info})