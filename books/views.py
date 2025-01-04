# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
import pymongo
from bson import Decimal128
from django.http import Http404
from decimal import Decimal
from rest_framework import permissions  # Importar permisos
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Avg
from django.db import connection


class BookListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        books = Book.objects.all()

        # Convertir el campo 'price' de Decimal128 a float antes de pasar al serializador
        for book in books:
            if isinstance(book.price, Decimal128):
                book.price = float(book.price.to_decimal())

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={201: BookSerializer}
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            #book_data = serializer.validated_data
            #book = Book(**book_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """

    permission_classes = [permissions.IsAuthenticated]
    #def get_object(self, title):
        #return Book.objects.filter(title=title)
    
    def get(self, request, title, format=None):
        try:
            # book= self.get_object(title)
            # serializer = BookSerializer(book)
            # return Response(serializer.data)
            book = Book.objects.get(title=title)
            data = {
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "genre": book.genre,
                "price": float(book.price),  # Convertimos Decimal128 a float
            }
            return Response(data)
        except Book.DoesNotExist:
            return Response({"error": "Book no encontrado"}, status=404)
    
    def get_object(self, title):
        try:
            return Book.objects.get(title=title)  # Usamos get para obtener un solo objeto
        except Book.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={200: BookSerializer}
    )
    def put(self, request, title, *args, **kwargs):
        book = self.get_object(title)

        if not book:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        # Usamos el serializer sin `many=True` porque solo queremos actualizar un libro
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,title, format= None):
        book = self.get_object(title)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Endpoint para obtener el precio promedio de los libros publicados en un año


from decimal import Decimal  # Importar para trabajar con Decimal
from bson import Decimal128  # Importar para trabajar con Decimal128

class BookAvgPriceByYearAPIView(APIView):
    def get(self, request, year):
        try:
            # Filtramos los libros publicados en el año especificado
            books = Book.objects.filter(published_date__year=year)

            if not books:
                return Response({"error": "No books found for the given year"}, status=status.HTTP_404_NOT_FOUND)

            # Calculamos el precio promedio de los libros filtrados
            total_price = 0
            for book in books:
                # Convertir Decimal128 a float si es necesario
                if isinstance(book.price, Decimal128):
                    # Convertimos Decimal128 a Decimal y luego a float
                    price_float = float(book.price.to_decimal())
                else:
                    price_float = float(book.price)

                total_price += price_float

            avg_price = total_price / len(books)

            return Response({"avg_price": avg_price}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'firstname': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                'lastname': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
            },
            required=['username', 'password']
        ),
        responses={201: openapi.Response('User created successfully')}
    )
    def post(self, request):
        print('request.data')
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('firstname')
        last_name = request.data.get('lastname')
        email = request.data.get('email')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)