from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import User

# user
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("id", "username", "email")


# register
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User(validated_data["username"], validated_data["email"])
            user.set_password(validated_data["password"])
            user.save()
            return user


# login


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
