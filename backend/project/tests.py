from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from mixer.backend.django import mixer

from .models import Project


class ProjectTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='test', password='qwerty')
        self.client.force_login(self.user)
        self.project = mixer.cycle(5).blend(Project)

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 5)

    def test_get_not_login(self):
        self.client.logout()
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_login(self.user)

    def tearDown(self) -> None:
        self.client.logout()
