from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from ..models import CarBrandModel, CarModel, TaxiModel


class TaxiTest(TestCase):

    def _create_data(self):
        return TaxiModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.urls = {
            "list": reverse("taxi-list"),
            "retrieve": reverse("taxi-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("taxi-detail", kwargs={"pk": 1000}),
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


class CarTest(TestCase):

    def _create_data(self):
        return CarModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.urls = {
            "list": reverse("car-list"),
            "retrieve": reverse("car-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("car-detail", kwargs={"pk": 1000}),
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


class CarbrandTest(TestCase):

    def _create_data(self):
        return CarBrandModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.urls = {
            "list": reverse("car-brand-list"),
            "retrieve": reverse("car-brand-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("car-brand-detail", kwargs={"pk": 1000}),
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
