from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def test_create_author(self):
        """
        Test for succesfully create author with name
        """

        author = models.Author.objects.create(
            name='lorem ipsum'
        )

        self.assertEqual(str(author), author.name)
        self.assertTrue(
            isinstance(author.author_id, int)
        )
