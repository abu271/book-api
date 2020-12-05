from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Book, Author


def create_author(full_name):
    author = Author.objects.create(
        name=full_name
    )
    return author


BOOK_URL = reverse("book:book-list")


class BookApiTests(TestCase):
    """
    Tests for book API
    """

    def setUp(self):
        self.client = APIClient()

    def test_create_book_success(self):
        """
        Test book is created successfuly
        """
        author_1 = create_author("Larry Lorem")

        payload = {
            'name': 'Django Cook Book',
            'edition': '2nd',
            'publication_year': 2005,
            'authors': [author_1.author_id]
        }
        res = self.client.post(BOOK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        test_book = Book.objects.get(book_id=res.data['book_id'])
        self.assertEqual(test_book.name, payload['name'])
