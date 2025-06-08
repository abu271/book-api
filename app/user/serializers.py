from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user objects
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password']
        read_only_fields = ['user_id', 'date_of_birth']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8
            }
        }

    #TODO: Add action decorator for listing users endpoint