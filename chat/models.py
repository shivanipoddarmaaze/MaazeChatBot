from django.db import models


class User(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ChatRoom(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name


class Group(models.Model):
    name = models.CharField(max_length=500)
    chat_room = models.ForeignKey(ChatRoom, related_name="chat_room", on_delete=models.CASCADE)
    group = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)


# class Lobby(models.Model):
#     chat_room = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, related_name="user", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
    def __str__(self):
        return self.name


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, related_name="user_room", on_delete=models.CASCADE)
    message_by = models.ForeignKey(User, related_name="message_by", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def last_10_messages(self):
        return Message.objects.order_by('-created_at').all()[:10]


