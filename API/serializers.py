from rest_framework import serializers, fields

from .models import UserData, MessageData


class MessageDataSerializer(serializers.ModelSerializer):

    date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%f'])

    class Meta:
        model = MessageData
        fields = [
            "message_id",
            "author_id",
            "content",
            "date"
        ]

    def create(self, data):
        user_id = data["author_id"]
        user = UserData.objects.get_or_create(user_id=user_id)[0]
        user.nb_msg += 1
        user.save()
        message = MessageData.objects.get_or_create(
            message_id=data["message_id"]
        )[0]
        message.author_id = data.get("author_id", message.author_id)
        message.content = data.get("content", message.content)
        message.date = data.get("date", message.date)
        message.save()
        return message


class UserDataSerializer(serializers.ModelSerializer):
    top = serializers.SerializerMethodField()

    class Meta:
        model = UserData
        ordering = ('nb_msg',)  # don't know what this does
        fields = [
            "user_id",
            "avatar_url",
            "name",
            "discriminator",
            "nb_msg",
            "top"
        ]

    def get_top(self, obj):
        allUsers = reversed(UserData.objects.all().order_by("nb_msg"))
        for i, user in enumerate(allUsers):
            if user == obj:
                return i+1

    def create(self, data):
        user_id = data.pop("user_id")
        user = UserData.objects.get_or_create(user_id=user_id)[0]
        user.avatar_url = data.get("avatar_url", user.avatar_url)
        user.name = data.get("name", user.name)
        user.discriminator = data.get("discriminator", user.discriminator)
        user.ghost = False
        user.save()
        return user
