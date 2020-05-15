from rest_framework import serializers;
from rent_server.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['title','text']
