from django.urls import path
from rest_framework.routers import DefaultRouter
from ecommerce.views.OrderViewSet import OrderViewSet
from ecommerce.views.OrderDetailViewSet import OrderDetailViewSet
from ecommerce.views.OrderList import OrderList


router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='orders')
router.register('orderlist',OrderList, basename='orderList')
router.register('orderdetail', OrderDetailViewSet, basename='orderDetail')

urlpatterns = [
] + router.urls