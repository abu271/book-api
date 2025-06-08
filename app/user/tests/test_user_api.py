from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import User

USER_URL = reverse("user:user-list")

def detail_url(user_id):
    """
    Return user detail URL
    """
    return reverse("user:user-detail", args=[user_id])

class UserCreateTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'strongpassword123',
            'date_of_birth': '1990-01-01',
            'gender': 'Other'
        }
        response = self.client.post(USER_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_create_user_missing_required_field(self):
        payload = {
            'first_name': 'Test',
            'email': 'testuser2@example.com',
            'password': 'strongpassword123',
            'gender': 'Other'
        }
        response = self.client.post(USER_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_duplicate_username(self):
        User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='password',
            gender='Other'
        )
        payload = {
            'username': 'testuser',
            'email': 'testuser2@example.com',
            'password': 'anotherpassword',
            'gender': 'Other'
        }
        response = self.client.post(USER_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_duplicate_email(self):
        User.objects.create(
            username='uniqueuser',
            email='testuser@example.com',
            password='password',
            gender='Other'
        )
        payload = {
            'username': 'testuser2',
            'email': 'testuser@example.com',
            'password': 'anotherpassword',
            'gender': 'Other'
        }
        response = self.client.post(USER_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='getuser',
            email='getuser@example.com',
            password='password',
            gender='Other'
        )

    def test_get_user_success(self):
        response = self.client.get(detail_url(self.user.user_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'getuser')

    def test_get_user_not_found(self):
        response = self.client.get(detail_url(9999))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
