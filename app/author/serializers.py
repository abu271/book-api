from rest_framework import serializers
from core.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for author objects
    """
    class Meta:
        model = Author
        fields = ['author_id', 'name']
        read_only_fields = ['author_id']
