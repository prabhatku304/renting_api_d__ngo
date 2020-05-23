from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializers
# Create your views here.


@api_view(['POST'])
def registeration_user(request):

    if request.method == 'POST':
        serializer = RegisterSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successful created new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.create(user=account).key
            print("hello............")
            print(token)
        else:
            data = serializer.errors

        return Response(data)
