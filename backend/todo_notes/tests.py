from django.test import TestCase
from django.contrib.auth.models import User as UserAuth

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from mixer.backend.django import mixer

from .views import TODO_NoteModelLimitedViewSet
from .models import TODO_Note


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = UserAuth.objects.create_superuser(username='test', password='qwerty')
        self.note = mixer.blend(TODO_Note)
        self.client = APIClient()

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = TODO_NoteModelLimitedViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_2(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def tearDown(self) -> None:
        self.client.logout()
