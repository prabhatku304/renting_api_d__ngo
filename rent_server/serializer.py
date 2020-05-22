from rest_framework import serializers
from 
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','title', 'text']
