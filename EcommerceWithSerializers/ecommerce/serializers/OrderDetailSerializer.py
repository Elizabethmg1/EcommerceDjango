from rest_framework import serializers
from ecommerce.models import OrderDetail

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('product_id','quantity','order_id')