from rest_framework import serializers
from bson import Decimal128  # Importa Decimal128 desde bson
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Convertir Decimal128 a float
        if isinstance(instance.price, Decimal128):
            representation['price'] = float(instance.price.to_decimal())
        
        return representation

    def validate_price(self, value):
        if isinstance(value, Decimal128):
            value = float(value)  # O Decimal(value)
        return value