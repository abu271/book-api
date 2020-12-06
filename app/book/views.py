from rest_framework import viewsets
from core.models import Book, Author
from book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Book viewset for basic C.R.U.D operations
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Return a list of filtered books if a param is 
        set otherwise return all of the books
        """
        name = self.request.query_params.get('name')
        publication_year = self.request.query_params.get('publication_year')
        author = self.request.query_params.get('author')

        if name is not None:
            book = Book.objects.filter(name=name)

        elif publication_year is not None:
            book = Book.objects.filter(publication_year=publication_year)

        elif author is not None:
            author = Author.objects.filter(name__icontains=author)
            author_id = author[0].author_id
            book = Book.objects.filter(authors=author_id)

        else:
            book = Book.objects.all()

        return book
