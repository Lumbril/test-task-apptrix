from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class UserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'gender',
                  'latitude', 'longitude']


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['email', 'password', 'first_name', 'last_name', 'avatar', 'gender',
                  'latitude', 'longitude']
