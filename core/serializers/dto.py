from rest_framework import serializers
from core.models import Category, Product

class CategoryDTO(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('key', 'title', 'subtitle', 'slug')

class ProductDTO(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('key', 'title', 'category', 'price')