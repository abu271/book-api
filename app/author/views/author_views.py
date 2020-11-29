from rest_framework import generics
from core.models import Author
from author.serializers import AuthorSerializer


class AuthorApi(generics.ListCreateAPIView):
    """
    API view to retrieve list of authors or create new
    """
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer


class AuthorCreateApi(generics.CreateAPIView):
    """
    API view to retrieve, update or delete author
    """
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer
