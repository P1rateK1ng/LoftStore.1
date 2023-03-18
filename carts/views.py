from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from carts.models import CartModel, CartItemModel
from carts import serializers



class CartItemViewSet(ModelViewSet):
    queryset = CartItemModel.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CartItemSerializer
        if self.action == 'create':
            return serializers.CreateCartItemSerializer
        if self.action == 'retrieve':
            return serializers.CartItemSerializer

class CartViewSet(ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = (permissions.IsAuthenticated,)