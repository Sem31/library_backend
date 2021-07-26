from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone','address', 'profile']

    def validate(self, data):
        user_obj = User(
            username=data.get('username'),
            phone = data.get('phone'),
            email=data.get('email')
        )
        user_obj.set_password(data.get('password'))
        user_obj.is_active = True
        user_obj.is_member = True
        user_obj.save()
        return user_obj

class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            auth = authenticate(email=email, password=password)
            if auth:
                return auth
            else:
                raise exceptions.ValidationError('Email or Password Invalid')
        else:
            raise exceptions.ValidationError('All Fields Required***')