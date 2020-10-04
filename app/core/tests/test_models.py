from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def test_create_author(self):
        """
        Test for succesfully create author with name
        """

        author = models.Author.objects.create(
            name='Joe Bloggs'
        )

        self.assertEqual(str(author), author.name)
        self.assertTrue(
            isinstance(author.author_id, int)
        )

    def test_create_book_with_one_author(self):
        """
        Test for creating a book with one author
        """

        book = models.Book.objects.create(
            name='Recipe Book',
            edition='2nd',
            publication_year=2005
        )
        book.save()

        author = book.authors.create(name='Jane Bloggs')
        author.save()

        self.assertEqual(book.authors.all()[0], author)
        self.assertEqual(author.name, 'Jane Bloggs')

        self.assertEqual(str(book), book.name)
        self.assertEqual(book.edition, '2nd')
        self.assertEqual(book.publication_year, 2005)
        self.assertTrue(
            isinstance(book.book_id, int)
        )

    def test_create_book_with_multiple_authors(self):
        """
        Test for creating a book with three authors
        """

        book = models.Book.objects.create(
            name='Photography Book',
            edition='1st',
            publication_year=2010
        )
        book.save()

        author1 = book.authors.create(name='Jane Bloggs')
        author1.save()

        author2 = book.authors.create(name='Lorem Ipsum')
        author2.save()

        author3 = book.authors.create(name='Steve Brick')
        author3.save()

        self.assertEqual(book.authors.all()[0], author1)
        self.assertEqual(author1.name, 'Jane Bloggs')

        self.assertEqual(book.authors.all()[1], author2)
        self.assertEqual(author2.name, 'Lorem Ipsum')

        self.assertEqual(book.authors.all()[2], author3)
        self.assertEqual(author3.name, 'Steve Brick')

        self.assertEqual(str(book), book.name)
        self.assertEqual(book.edition, '1st')
        self.assertEqual(book.publication_year, 2010)
        self.assertTrue(
            isinstance(book.book_id, int)
        )
