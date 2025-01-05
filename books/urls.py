# urls.py

from django.urls import path
from .views import  BookListAPIView, BookDetail, BookAvgPriceByYearAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    #path('books/<str:title>/', BookDetail.as_view()),
    path('<str:title>/', BookDetail.as_view(), name='book-detail'),
    #path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('avg-price/<int:year>/', BookAvgPriceByYearAPIView.as_view(), name='book-avg-price-by-year')

]
