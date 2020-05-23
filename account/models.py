from django.db import models
from datetime import datetime, timedelta
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
import jwt

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("username must be for Users")
        if email is None:
            raise TypeError("email must be of User")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)


class User(models.Model):

    name = models.CharField(max_length=64)
    username = models.TextField()
    password = models.CharField(max_length=20)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def token(self):

        timer = datetime.now() + timedelta(days=60)
        payloads = {}
        payloads['email'] = self.email
        payloads['pk'] = self.pk
        payloads['exp'] = int(timer.strftime("%s"))

        tokens = jwt.encode(payloads, settings.SECRET_KEY, algorithm='HS256')
        return tokens.decode('UTF-8')


# If you want every user to have an automatically generated Token, you can simply catch the User's post_save signal.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
