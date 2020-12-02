from rest_framework import serializers
from core.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for book objects
    """
    class Meta:
        model = Book
        fields = ["book_id", "name", "publication_year", "edition", "authors"]
        read_only_fields = ["book_id"]
