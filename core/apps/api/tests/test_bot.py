from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from core.apps.shared.utils.jwt import make_bot_jwt

from ..models import BotModel, BotUserModel


class BotTest(TestCase):

    def _create_data(self):
        return BotModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_TOKEN=make_bot_jwt())
        self.instance = self._create_data()
        self.urls = {
            "retrieve": reverse("bot-detail", kwargs={"pk": self.instance.tg_id}),
            "retrieve-not-found": reverse("bot-detail", kwargs={"pk": 1000}),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve_not_found(self):
        response = self.client.get(self.urls["retrieve-not-found"])
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 404)


class BotuserTest(TestCase):

    def _create_data(self):
        return BotUserModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_TOKEN=make_bot_jwt())
        self.instance = self._create_data()
        self.urls = {
            "list": reverse("bot-user-list"),
            "retrieve": reverse("bot-user-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("bot-user-detail", kwargs={"pk": 1000}),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_list(self):
        response = self.client.get(self.urls["list"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve_not_found(self):
        response = self.client.get(self.urls["retrieve-not-found"])
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 404)
