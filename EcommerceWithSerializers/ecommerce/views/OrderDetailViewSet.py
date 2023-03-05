from rest_framework import viewsets
from ecommerce.serializers.OrderDetailSerializer import OrderDetailSerializer
from ecommerce.models import OrderDetail

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer