from rest_framework import serializers
from core.models import Category, Product

class CategoryDTO(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'subtitle')

class ProductDTO(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'subtitle', 'category')