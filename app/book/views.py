from rest_framework import viewsets
from core.models import Book
from book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Book viewset for basic C.R.U.D operations
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
