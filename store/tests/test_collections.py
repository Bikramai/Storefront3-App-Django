from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_not_anonymous_return_401(self):
        #AAA(Arrange, Act, Assert)

        # Act
        client = APIClient()
        response = client.post('/store/collections/', { 'title': 'a' })

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

