from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from carts.models import CartModel
from carts.serializers import CartSerializer


class CartViewSet(ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
