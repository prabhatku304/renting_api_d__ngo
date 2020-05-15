from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializer import MessageSerializer

@api_view(['GET'])
def message_api(request):
    message = Message.objects.all()

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)
