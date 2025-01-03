# scripts/migrate_books.py

from datetime import datetime
from books.models import Book

def insert_books():
    books = [
        {"title": "Book 1", "author": "Author A", "published_date": "2020-06-15", "genre": "Fiction", "price": 19.99},
        {"title": "Book 2", "author": "Author B", "published_date": "2020-07-15", "genre": "Non-fiction", "price": 15.49},
        {"title": "Book 3", "author": "Author C", "published_date": "2021-06-20", "genre": "Fiction", "price": 22.99},
        {"title": "Book 4", "author": "Author D", "published_date": "2021-06-18", "genre": "Fiction", "price": 24.99},
        {"title": "Book 5", "author": "Author E", "published_date": "2022-05-10", "genre": "Sci-Fi", "price": 12.99},
    ]
    
    for book_data in books:
        book = Book(**book_data)
        book.save()
        
insert_books()
