from rest_framework import viewsets
from ecommerce.models import Order
from ecommerce.serializers.OrderSerializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer