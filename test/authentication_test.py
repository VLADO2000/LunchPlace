import pytest
from rest_framework.test import APIClient
from django.contrib.auth.hashers import check_password
from authentication.models import CustomUser

@pytest.mark.django_db
class TestAuthentication:

    def test_user_registration(self):
        client = APIClient()
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'password',
            'role': 0,  # Role 0 for viewers
        }
        response = client.post('/custom-auth/api/v1/user/', data, format='json')
        assert response.status_code == 201
        assert CustomUser.objects.count() == 1
        assert check_password('password', CustomUser.objects.first().password)

    def test_user_login(self):
        client = APIClient()
        user = CustomUser.objects.create_user(
            name='Test User',
            email='testuser@example.com',
            password='testpassword',
            role=1,  # Role 1 for restaurateurs
        )
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = client.post('/custom-auth/api/v1/login/', data, format='json')
        assert response.status_code == 200
        assert 'token' in response.data

    def test_user_logout(self):
        client = APIClient()
        user = CustomUser.objects.create_user(
            name='Test User',
            email='testuser@example.com',
            password='testpassword',
            role=0,
        )
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = client.post('/custom-auth/api/v1/login/', data, format='json')
        assert response.status_code == 200
        token = response.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.post('/custom-auth/api/v1/logout/')
        assert response.status_code == 200