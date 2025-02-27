from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Book, Author


def sample_author(name):
    """
    Create and return sample author
    """
    return Author.objects.create(name=name)


def sample_book(name):
    """
    Create and return sample book
    """
    return Book.objects.create(
        name=name,
        edition='2nd',
        publication_year=2005
    )


def detail_url(book_id):
    """
    Return book detail URL
    """
    return reverse("book:book-detail", args=[book_id])


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
        author_1 = sample_author("Larry Lorem")

        payload = {
            'name': 'Django Cook Book',
            'edition': '2nd',
            'publication_year': 2005,
            'authors': [author_1.name]
        }
        res = self.client.post(BOOK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        test_book = Book.objects.get(book_id=res.data['book_id'])
        self.assertEqual(test_book.name, payload['name'])

    def test_list_book_success(self):
        """
        Test books is listed successfuly
        """

        book_1 = sample_book('Test Book')
        book_2 = sample_book('Another Book')

        res = self.client.get(BOOK_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertIn(book_1.name, res.data[0]['name'])
        self.assertIn(book_2.name, res.data[1]['name'])

    def test_detail_view_book_success(self):
        """
        Test succesfully view one book
        """

        book_1 = sample_book('The Story of Lorem Ipsum')
        URL = detail_url(book_1.book_id)

        res = self.client.get(URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(book_1.name, res.data['name'])

    def test_update_book_success(self):
        """
        Test succesfully edit book
        """
        author_1 = sample_author('Pluto')
        book_1 = sample_book('Tom & Jerry')
        book_id = Book.objects.get(name=book_1).book_id

        URL = detail_url(book_id)

        data = {
            'name': 'Looney Toons',
            'edition': '4th',
            'publication_year': 2019,
            'authors': [author_1.name]
        }
        res = self.client.put(URL, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(book_id, res.data['book_id'])
        self.assertIn(author_1.name, res.data['authors'])
        self.assertNotEqual(book_1.name, res.data['name'])
        self.assertNotEqual(
            book_1.publication_year,
            res.data['publication_year']
        )
        self.assertNotEqual(book_1.edition, res.data['edition'])

    def test_delete_book_success(self):
        """
        Test succesfully delete book
        """
        book_1 = sample_book('Fake book')
        book_id = Book.objects.get(name=book_1).book_id
        URL = detail_url(book_id)

        res = self.client.delete(URL)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_book_by_name_success(self):
        """
        Test filter books by name successfuly
        """

        book_1 = sample_book('Filter By Name Book')
        sample_book('Another Book')

        res = self.client.get(BOOK_URL, {'name': 'Filter By Name Book'})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(book_1.name, res.data[0]['name'])

    def test_filter_book_by_publication_year_success(self):
        """
        Test filter books by when it was published successfuly
        """
        author_1 = sample_author('Boris')

        payload = {
            'name': '2012 London Olympics Photo Album',
            'edition': '1st',
            'publication_year': 2012,
            'authors': [author_1.name]
        }

        book_1 = self.client.post(BOOK_URL, payload).data
        sample_book('Another Book')

        res = self.client.get(BOOK_URL, {'publication_year': 2012})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(book_1['name'], res.data[0]['name'])

    def test_filter_book_by_author_name_success(self):
        """
        Test filter books by author's name successfuly
        """
        author_1 = sample_author('John Steinbeck')

        payload = {
            'name': 'Of Mice and Men',
            'edition': '1st',
            'publication_year': 1937,
            'authors': [author_1.name]
        }

        book_1 = self.client.post(BOOK_URL, payload).data
        sample_book('Another Book')

        res = self.client.get(BOOK_URL, {'author': 'steinbeck'})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(book_1['name'], res.data[0]['name'])
