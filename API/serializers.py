from rest_framework import serializers, fields

from .models import UserData, MessageData


class MessageDataSerializer(serializers.ModelSerializer):

    date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])

    class Meta:
        model = MessageData
        fields= '__all__'

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'
