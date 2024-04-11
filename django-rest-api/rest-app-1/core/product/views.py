from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


@api_view(["GET", "POST", "PUT", "DELETE"])
def ProductView(request, id=None):

    # get all products
    if request.method == "GET":
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(
            {
                "message": "All Products Data",
                "status": status.HTTP_200_OK,
                "data": serializer.data,
            }
        )

    # create a new product
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Product Created",
                    "status": status.HTTP_201_CREATED,
                    "data": serializer.data,
                }
            )
        else:
            return Response(
                {
                    "message": "Invalid Data",
                    "status": status.HTTP_400_BAD_REQUEST,
                    "error": serializer.errors,
                }
            )

    # update a product
    if request.method == "PUT":
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Product Updated",
                    "status": status.HTTP_200_OK,
                    "data": serializer.data,
                }
            )
        else:
            return Response(
                {
                    "message": "Invalid Data",
                    "status": status.HTTP_400_BAD_REQUEST,
                    "error": serializer.errors,
                }
            )

    # delete a product
    if request.method == "DELETE":
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        product.delete()
        return Response(
            {
                "message": "Product Deleted",
                "status": status.HTTP_200_OK,
                "data": serializer.data,
            }
        )

    # handle error for invalid request
    return Response(
        {
            "message": "Invalid Request",
            "status": status.HTTP_400_BAD_REQUEST,
            "data": [],
        }
    )
