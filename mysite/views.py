from django.shortcuts import render, redirect
from chat.models import *


def home(request):
    if request.method == "POST":
        try:
            group = Group.objects.filter(chat_room=request.POST["user"])
            request.user = User.objects.get(id=request.POST["user"]).name
            return render(request, "room.html", context={"groups": group})
        except:
            return redirect("room", request.POST["group"])
    chat = ChatRoom.objects.all()
    return render(request, "home.html", context={"chats": chat})
#
#
# def room(request, room_name):
#     return render(request, "chat/room.html", {"room_name": room_name})