from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Author


AUTHOR_URL = reverse("author:author-list")


def sample_author(name):
    """
    Create and return sample author
    """
    return Author.objects.create(name=name)


def detail_url(author_id):
    """
    Return author detail URL
    """
    return reverse("author:author-detail", args=[author_id])


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
        res = self.client.post(AUTHOR_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        test_author = Author.objects.get(author_id=res.data['author_id'])
        self.assertEqual(test_author.name, payload['name'])

    def test_list_author_success(self):
        """
        Test authors is listed successfuly
        """

        author_1 = sample_author('Lorem Ipsum')
        author_2 = sample_author('Mac Nelly')

        res = self.client.get(AUTHOR_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertIn(author_1.name, res.data[0]['name'])
        self.assertIn(author_2.name, res.data[1]['name'])

    def test_detail_view_author_success(self):
        """
        Test succesfully view one author
        """

        author_1 = sample_author('Lorem Ipsum')
        URL = detail_url(author_1.author_id)

        res = self.client.get(URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(author_1.name, res.data['name'])

    def test_update_author_success(self):
        """
        Test succesfully edit author
        """
        author_1 = sample_author('Jackson Sully')
        author_id = Author.objects.get(name=author_1).author_id
        URL = detail_url(author_id)

        data = {
            'name': 'Tom Paul'
        }
        res = self.client.put(URL, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(author_id, res.data['author_id'])
        self.assertNotEqual(author_1.name, res.data['name'])

    def test_delete_author_success(self):
        """
        Test succesfully delete author
        """
        author_1 = sample_author('Fake Author')
        author_id = Author.objects.get(name=author_1).author_id
        URL = detail_url(author_id)

        res = self.client.delete(URL)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
