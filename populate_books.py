from decimal import Decimal
import os
import django
from datetime import date

# Configura el entorno Django para que puedas acceder a los modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')  # Reemplaza 'myproject' con el nombre de tu proyecto
django.setup()

from books.models import Book  # Reemplaza 'myapp' con el nombre de tu aplicación

def populate_books():
    # Lista de libros con precios como Decimal
    books = [
        {
            'title': 'Cien años de soledad',
            'author': 'Gabriel García Márquez',
            'published_date': date(1967, 6, 5),
            'genre': 'Realismo mágico',
            'price': Decimal('39.99')  # Mantén como Decimal para controlar la conversión
        },
        {
            'title': 'Don Quijote de la Mancha',
            'author': 'Miguel de Cervantes',
            'published_date': date(1605, 1, 1),
            'genre': 'Novela',
            'price': Decimal('29.99')
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'published_date': date(1949, 6, 8),
            'genre': 'Distopía',
            'price': Decimal('19.99')
        },
        {
            'title': 'La sombra del viento',
            'author': 'Carlos Ruiz Zafón',
            'published_date': date(2001, 4, 6),
            'genre': 'Suspense',
            'price': Decimal('25.99')
        }
    ]
    
    # Convertir los precios a float antes de insertarlos en la base de datos
    for book_data in books:
        book_data['price'] = float(book_data['price'])  # Asegurarse de que el precio es un float
        
        book, created = Book.objects.get_or_create(**book_data)
        if created:
            print(f"Libro '{book.title}' creado exitosamente.")
        else:
            print(f"Libro '{book.title}' ya existía.")

if __name__ == '__main__':
    populate_books()
