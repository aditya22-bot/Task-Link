from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Signup
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password


# Register serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['id', 'username', 'Email', 'Password', 'Address']
        extra_kwargs = {
            'Password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SingnupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'username', 'Email', 'Address')


class ChangePasswordSerializer(serializers.Serializer):
    model = Signup

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
