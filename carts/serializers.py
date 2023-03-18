from rest_framework import serializers
from carts.models import CartModel, CartItemModel
from products.models import ProductModel


class SimpleProduct(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProduct(many=False)
    sub_total = serializers.SerializerMethodField(method_name='total')
    class Meta:
        model = CartItemModel
        fields = ['id', 'product', 'count', 'user', 'sub_total']

    def total(self, cartItem:CartItemModel):
        return cartItem.count * cartItem.product.price


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = "__all__"

class CreateCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItemModel
        fields = "__all__"
