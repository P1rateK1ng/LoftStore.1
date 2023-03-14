from rest_framework.serializers import ModelSerializer
from products.models import ProductModel, ProductCategoryModel


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"