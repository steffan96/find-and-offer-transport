from rest_framework import serializers
from chat.models import ChatBox, Message


class ChatBoxSerializer(serializers.HyperlinkedModelSerializer):
    pass