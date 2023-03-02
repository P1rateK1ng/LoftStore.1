from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from products.serializers import ProductSerializer
from products.models import Product


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def apiOverview(request):
	api_urls = {
		'List':'/list/',
		# 'Detail View':'/detail/<str:pk>/',
		# 'Create':'/create/',
		# 'Update':'/update/<str:pk>/',
		# 'Delete':'/delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def productList(request):
	product = Product.objects.all().order_by('-id')
	serializer = ProductSerializer(product, many=True)
	return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def productDetail(request, pk):
# 	product = Product.objects.get(id=pk)
# 	serializer = ProductSerializer(product, many=False)
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def productCreate(request):
# 	serializer = ProductSerializer(data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def productUpdate(request, pk):
# 	product = Product.objects.get(id=pk)
# 	serializer = ProductSerializer(instance=product, data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['DELETE'])
# def productDelete(request, pk):
# 	product = Product.objects.get(id=pk)
# 	product.delete()
#
# 	return Response('Product succsesfully delete!')
