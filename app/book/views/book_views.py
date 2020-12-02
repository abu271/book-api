from rest_framework import generics
from core.models import Book
from book.serializers import BookSerializer


class BookApi(generics.ListAPIView):
    """
    API view to retrieve list of books
    """
    queryset = Book.objects.all().order_by("name")
    serializer_class = BookSerializer


class BookCreateApi(generics.CreateAPIView):
    """
    API view to create book
    """
    queryset = Book.objects.all().order_by("name")
    serializer_class = BookSerializer
