from django.urls import path

from carts.views import CartViewSet, CartItemViewSet

app_name = 'carts'

urlpatterns = [
    # carts
    path('', CartViewSet.as_view({'get': 'list'}), name='api-CartViewSet'),
    path('<str:pk>/', CartViewSet.as_view({'get': 'retrieve'}), name='api-Cart-Retrieve-ViewSet'),
    path('create/', CartViewSet.as_view({'post': 'create'}), name='api-Cart-Create-ViewSet'),
    # cart items
    path('items/', CartItemViewSet.as_view({'get': 'list'}), name='api-CartItem-ViewSet'),
    path('items/<str:pk>/', CartItemViewSet.as_view({'get': 'retrieve'}), name='api-CartItem-Retrieve-ViewSet'),
    path('items/create/', CartItemViewSet.as_view({'post': 'create'}), name='api-CartItem-Create-ViewSet'),
]