from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/products/",
        "/api/products/<id>/",
        "/api/products/create/",
        "/api/products/upload/",
        "/api/products/<id>/reviews",
        "/api/products/top/",
        "/api/products/delete/<id>/",
        "/api/products/<update/<id>/",
    ]
    return Response(routes)


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response("Product of id {} not found".format(pk), status=404)

    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)
