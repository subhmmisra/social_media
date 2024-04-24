from rest_framework import serializers
from apps.users import services as user_services
from apps.users.models import UserManager, User
import re



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)


# class AuthUserSerializer(serializers.Serializer):
#     user = serializers.


