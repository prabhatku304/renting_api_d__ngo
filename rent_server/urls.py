from django.urls import path
from .views import message_api

app_name = 'rent-server'

urlpatterns = [
     path('message/',message_api, name = 'message_list')
]
