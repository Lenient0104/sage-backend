from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class MyViewSetTestCase(APITestCase):
    def test_list_view(self):
        response = self.client.get('/my-viewset/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'John')
