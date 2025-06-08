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

    def test_create_user_with_required_fields(self):
        """
        Test creating a user with required fields only
        """
        user = models.User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            gender='Other'
        )
        self.assertEqual(str(user), user.username)
        self.assertTrue(isinstance(user.user_id, int))
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.gender, 'Other')

    def test_create_user_with_all_fields(self):
        """
        Test creating a user with all fields
        """
        user = models.User.objects.create(
            username='janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.com',
            password='securepassword',
            date_of_birth='1995-05-15',
            gender='Female',
            ethnicity='Asian',
            religion='None'
        )
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.date_of_birth, '1995-05-15')
        self.assertEqual(user.ethnicity, 'Asian')
        self.assertEqual(user.religion, 'None')

    def test_user_unique_username(self):
        """
        Test that creating a user with a duplicate username raises an error
        """
        models.User.objects.create(
            username='uniqueuser',
            email='unique1@example.com',
            password='password',
            gender='Other'
        )
        with self.assertRaises(Exception):
            models.User.objects.create(
                username='uniqueuser',
                email='unique2@example.com',
                password='password',
                gender='Other'
            )

    def test_user_unique_email(self):
        """
        Test that creating a user with a duplicate email raises an error
        """
        models.User.objects.create(
            username='userone',
            email='uniqueemail@example.com',
            password='password',
            gender='Other'
        )
        with self.assertRaises(Exception):
            models.User.objects.create(
                username='usertwo',
                email='uniqueemail@example.com',
                password='password',
                gender='Other'
            )
