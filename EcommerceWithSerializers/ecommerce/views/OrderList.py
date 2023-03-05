from rest_framework.viewsets import ReadOnlyModelViewSet
from ecommerce.serializers.OrderSerializer import OrderSerializer
from ecommerce.models import Order

class OrderList(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    lookup_field = 'slug'
    queryset = Order.objects.all()