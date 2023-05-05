from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["address", "positions"]

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for p in positions:
            stok_product = StockProduct.objects.create(product=p['product'], stock=stock, quantity=p['quantity'], price=p['price'])
            stock.positions.add(stok_product)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for p in positions:
            StockProduct.objects.update_or_create(defaults={'quantity': p['quantity'], 'price': p['price']}, product=p['product'], stock=stock)
        return stock
