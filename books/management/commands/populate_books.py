from django.core.management.base import BaseCommand
from books.models import Book
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample books'

    def handle(self, *args, **kwargs):
        sample_books = [
            {'title': 'Book 1', 'author': 'Author 1', 'published_date': date(2020, 1, 1), 'genre': 'Fiction', 'price': 19.99},
            {'title': 'Book 2', 'author': 'Author 2', 'published_date': date(2021, 5, 15), 'genre': 'Non-Fiction', 'price': 24.99},
            {'title': 'Book 3', 'author': 'Author 3', 'published_date': date(2020, 8, 30), 'genre': 'Fantasy', 'price': 15.99},
            {'title': 'Book 4', 'author': 'Author 4', 'published_date': date(2022, 2, 20), 'genre': 'Science Fiction', 'price': 29.99},
            {'title': 'Book 5', 'author': 'Author 5', 'published_date': date(2021, 7, 10), 'genre': 'Mystery', 'price': 14.99},
        ]
        for book in sample_books:
            Book.objects.create(**book)
        self.stdout.write('Sample books added.')
