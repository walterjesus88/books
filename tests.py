# tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def test_create_book(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2023-05-01',
            'genre': 'Drama',
            'price': 20.99
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_avg_price_by_year(self):
        url = reverse('book-avg-price', args=[2021])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
