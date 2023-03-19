from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from products.serializers import ProductSerializer, ProductCategorySerializer
from products.models import ProductModel, ProductCategoryModel


class ProductCategoryViews(ModelViewSet):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (permissions.AllowAny,)


class ProductViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)