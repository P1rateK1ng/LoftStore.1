from django.contrib import admin

from carts.models import CartModel, CartItemModel


@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']
    list_filter = ['created_at']
    empty_value_display = '-пусто-'


@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart']
    search_fields = ['id']
    list_filter = ['id']
    empty_value_display = '-пусто-'