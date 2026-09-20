from rest_framework import serializers
from .models import Cart
from products.models import Product
from products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
            queryset=Product.objects.all(), source='product', write_only=True)
    quantity = serializers.IntegerField()
    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_id', 'quantity']

    def validate(self, data):
        product = data.get('product') or (self.instance.product if self.instance else None)
        quantity = data.get('quantity', self.instance.quantity if self.instance else None)

        if quantity > product.quantity:
            raise serializers.ValidationError(
                "Requested Quantity exceeds available Stock"
            )
        return data