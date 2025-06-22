from rest_framework import serializers
from rest_framework.response import Response
from core.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user objects
    """
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'date_of_birth']
        read_only_fields = ['user_id']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8
            }
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    # TODO: Add action decorator for listing users endpoint
