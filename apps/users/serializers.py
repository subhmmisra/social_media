from apps.users.models import User, UserManager
from rest_framework import serializers
from apps.users import services as user_services
import re


class RegisterBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "phone_number"
        ]
        model = User

    def validate_email(self, value):
        user = user_services.get_user_by_email(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken.")
        return UserManager.normalize_email(value)

    def validate_phone_number(self, value):
        if value:
            pattern = re.compile(r'^[6789]\d{9}$')
            if bool(pattern.match(value)):
                return value


class RegisterResponseSerializer(RegisterBaseSerializer):

    class Meta(RegisterBaseSerializer.Meta):
        fields = RegisterBaseSerializer.Meta.fields + ["full_name"]