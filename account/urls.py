from django.urls import path
from .views import registeration_user

app_name = "account"

urlpatterns = [
    path('register',registeration_user, name="register")
]