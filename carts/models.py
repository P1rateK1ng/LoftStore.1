import uuid
from django.db import models
from products.models import ProductModel
from users.models import UserModel


class CartModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class CartItemModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, verbose_name='корзина', related_name='items')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='покупатель', related_name='user')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='продукт', related_name='products')
    count = models.PositiveIntegerField(default=0, verbose_name='количество продукта в корзине')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"