from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Author


CREATE_AUTHOR_URL = reverse("author:create")


class AuthorApiTests(TestCase):
    """
    Tests for author API
    """

    def setUp(self):
        self.client = APIClient()

    def test_create_author_success(self):
        """
        Test author is created successfuly
        """
        payload = {'name': 'Joe Bloggs'}
        res = self.client.post(CREATE_AUTHOR_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        test_author = Author.objects.get(author_id=res.data['author_id'])
        self.assertEqual(test_author.name, payload['name'])
