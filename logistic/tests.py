from unittest import TestCase
from rest_framework.test import APIClient
class TestSampleView(TestCase):
    def test_sample_view(self):
        client = APIClient()
        url = '/api/v1/test/'
        responce = client.get(url)
        self.assertEqual(responce.data, "Hello world!")