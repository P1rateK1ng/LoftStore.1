from django.urls import path
from carts.views import CartViewSet
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', CartViewSet.as_view({'get':'list'}), name='cart_viewset'),
    path('create/', CartViewSet.as_view({'post':'create'}), name='cart_create_viewset'),
]