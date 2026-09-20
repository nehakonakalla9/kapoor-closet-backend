from rest_framework import serializers
from .models import Product, Style, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class StyleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Style
        fields = ['id', 'name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    style = StyleSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'style', 'color', 'size', 'quantity', 'description', 'price', 'image']