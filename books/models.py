from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title

