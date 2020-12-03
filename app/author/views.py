from rest_framework import generics
from core.models import Author
from author.serializers import AuthorSerializer


class AuthorApi(generics.ListAPIView):
    """
    API view to retrieve list of authors
    """
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer


class AuthorCreateApi(generics.CreateAPIView):
    """
    API view to create author
    """
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer
