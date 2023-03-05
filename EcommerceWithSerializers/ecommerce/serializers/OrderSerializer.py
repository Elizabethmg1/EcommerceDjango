from rest_framework import serializers
from ecommerce.models import Order
from ecommerce.serializers.OrderDetailSerializer import OrderDetailSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = OrderDetailSerializer(read_only=True, many=True)
    class Meta:
        model=Order
        fields = ('date','client','products')