from django.contrib import admin
from .models import Message, User, Group, ChatRoom

admin.site.register(Message)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(ChatRoom)