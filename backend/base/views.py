from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products

# Create your views here.

@api_view(['GET'])
def getRoutes (request):
    routes = [
        '/api/products/',
        '/api/products/<id>/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews',
        '/api/products/top/',
        '/api/products/delete/<id>/',
        '/api/products/<update/<id>/',
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts (request):
    return Response(products)


@api_view(['GET'])
def getProduct (request, pk):
    product = None

    for i in products:
        if str(i['_id']) == str(pk):
            product = i
            break
    
    if product is None:
        return Response("Product of id {} not found".format(pk), status=404)

    return Response(product)