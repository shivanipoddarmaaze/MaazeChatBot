import json
from .models import *
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        # print(User)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        name = text_data_json["name"]
        user = User.objects.get(name=name)
        chatroom = ChatRoom.objects.get(id=self.room_name)
        Message.objects.create(chat_room=chatroom, message_by=user, message=message)
        # self.sender = user.name
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, "sender": user.name}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "sender": sender}))