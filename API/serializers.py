from rest_framework import serializers, fields

from .models import UserData, MessageData


class MessageDataSerializer(serializers.ModelSerializer):

    date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%f'])

    class Meta:
        model = MessageData
        fields = '__all__'

    def create(self, data):
        user_id = data["author_id"]
        user = UserData.objects.get_or_create(user_id=user_id)[0]
        user.nb_msg += 1
        user.save()
        message = MessageData.objects.get_or_create(
            message_id=data["message_id"])[0]
        message.author_id = data.get("author_id", message.author_id)
        message.content = data.get("content", message.content)
        message.date = data.get("date", message.date)
        message.save()
        return message


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'

    def create(self, data):
        user_id = data.pop("user_id")
        user = UserData.objects.get_or_create(user_id=user_id)[0]
        user.avatar_url = data.get("avatar_url", user.avatar_url)
        user.name = data.get("name", user.name)
        user.discriminator = data.get("discriminator", user.discriminator)
        user.ghost = False
        user.save()
        return user
