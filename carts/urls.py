from django.urls import path

from carts.views import CartViewSet, CartItemViewSet, TestCartItemViewSet

app_name = 'carts'

urlpatterns = [
    path('', CartViewSet.as_view({'get': 'list'}), name='api-CartViewSet'),
    path('create/', CartViewSet.as_view({'post': 'create'}), name='api-CartViewSetCreate'),
    path('items/', CartItemViewSet.as_view({'get': 'list'}), name='api-CartItemViewSet'),
    path('items/create/', TestCartItemViewSet.as_view({'post': 'create'}), name='api-CartItemViewSetCreate'),
]