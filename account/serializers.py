from rest_framework import serializers
from .models import User


class RegisterSerializers(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name','email', 'username', 'password','password2']
        # adding extra keyword arguments here on password as security reason no one can read this

        extra_kwargs = {                   
            'password':{'write_only':True}
        }

    def save(self):

        account = User(
              email = self.validated_data['email'],
              username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password!=password2:
            return serializers.ValidationError({"password":"confirm password is not match"})

        account.password = password
        account.save()
        return account
