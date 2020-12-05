from rest_framework import viewsets
from core.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author viewset for basic C.R.U.D operations
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
