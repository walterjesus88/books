from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Book
from books.serializers import BookSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

#Pruebas para el Endpoint GET (list)
class BookListTests(APITestCase):
    def setUp(self):
        # Crea libros de prueba
        Book.objects.create(title="Cien años de soledad", author="Gabriel García Márquez", price=10)
        Book.objects.create(title="Don Quijote de la Mancha", author="Miguel de Cervantes", price=15)

    def test_get_books_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_books_list_500_error(self):
        response = self.client.get('/api/books/?error=true')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("detail", response.data)

# #Pruebas para el Endpoint POST
class BookCreateTests(APITestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Crea el token de acceso usando SimpleJWT
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        # Establece las credenciales en la solicitud
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_book(self):
        data = {
            "title": "Libro de los espiritus",
            "author": "Allan Kardec",
            "published_date": "2024-01-01",
            "genre": "Fiction",
            "price": 19.99
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_create_book_500_error(self):
        data = {
            "title": "Error",
            "author": "New Author",
            "published_date": "2024-01-01",
            "genre": "Fiction",
            "price": 19.99
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("detail", response.data)
