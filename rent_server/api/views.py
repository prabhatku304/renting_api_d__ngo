from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rent_server.models import Message
from rent_server.api.serializers import MessageSerializer

@api_view([]'GET'])
def message_view(request):
    try:
        message = Message.object.all()
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)
