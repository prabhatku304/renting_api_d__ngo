from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=64)
    username = models.TextField()
    password = models.CharField(max_length=20)
    email = models.EmailField()

    USERNAME_FIELD = 'username'


# If you want every user to have an automatically generated Token, you can simply catch the User's post_save signal.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
