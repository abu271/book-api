from rest_framework import serializers
from core.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for book objects
    """
    authors = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
    )
    class Meta:
        model = Book
        fields = ["book_id", "name", "publication_year", "edition", "authors"]
        read_only_fields = ["book_id"]
