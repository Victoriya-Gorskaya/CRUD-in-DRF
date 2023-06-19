from rest_framework.test import APIClient
from unittest import TestCase


class SampleTestCase(TestCase):
    def test_successful_request(self):
        client = APIClient()
        url = '/api/v1/test/'
        response = client.get(url)
        self.assertEqual(response.data, "Hello world!")


