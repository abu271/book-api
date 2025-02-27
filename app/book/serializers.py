from rest_framework import serializers
from core.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for book objects
    """
    authors = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        queryset=Author.objects.all()
    )
    class Meta:
        model = Book
        fields = ["book_id", "name", "publication_year", "edition", "authors"]
        read_only_fields = ["book_id"]
