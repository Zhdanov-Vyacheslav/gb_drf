from django.test import TestCase
from django.contrib.auth.models import User as UserAuth

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from mixer.backend.django import mixer

from .views import UserModelLimitedViewSet
from .models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user_auth = UserAuth.objects.create_superuser(username='test', password='qwerty')
        self.user = mixer.blend(User)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelLimitedViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_2(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user_auth)
        view = UserModelLimitedViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

