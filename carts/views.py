from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from carts.models import CartModel, CartItemModel
from carts.serializers import CartItemSerializer, CartSerializer, TestCartItemSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItemModel.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CartViewSet(ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TestCartItemViewSet(ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = TestCartItemSerializer
    permission_classes = (permissions.IsAuthenticated,)