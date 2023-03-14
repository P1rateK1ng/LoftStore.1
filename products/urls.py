from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, ProductCategoryViews

app_name = 'products'

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name='api-ProductViewSet'),
    path('create/', ProductViewSet.as_view({'post': 'create'}), name='api-ProductViewSetCreate'),
]
router = DefaultRouter()
router.register(r'category', ProductCategoryViews, basename="category")
urlpatterns += router.urls
