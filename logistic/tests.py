from rest_framework.test import APIClient
from unittest import TestCase


class SampleTestCase(TestCase):
    def test_successful_request(self):
        url = '/api/v1/test/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_bad_case(self):
        url = '/api/v1/sample/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
