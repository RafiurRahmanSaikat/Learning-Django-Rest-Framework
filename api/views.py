# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer

# Create your views here.


# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse(
#         {"data": serializer.data},
#     )
@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_details(request, pr):
    product = get_object_or_404(Product, pk=pr)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
