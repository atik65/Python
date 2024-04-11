from django.shortcuts import HttpResponse, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Home
from .serializers import HomeSerializer

# Create your views here.


# home get view
@api_view(["GET"])
def home(request):
    homeData = Home.objects.all()

    serializer = HomeSerializer(homeData, many=True)
    return Response(serializer.data)


# home post view
@api_view(["POST"])
def home_post(request):

    serializer = HomeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Data saved successfully",
                "status": status.HTTP_201_CREATED,
                "data": serializer.data,
            }
        )
    return Response(
        {
            "message": "Data not saved",
            "status": status.HTTP_400_BAD_REQUEST,
            "data": serializer.errors,
        }
    )


# home put view
@api_view(["PUT"])
def home_put(request, id):

    homeData = Home.objects.get(id=id)
    serializer = HomeSerializer(instance=homeData, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Data updated successfully",
                "status": status.HTTP_200_OK,
                "data": serializer.data,
            }
        )

    return Response(
        {
            "message": "Data not updated",
            "status": status.HTTP_400_BAD_REQUEST,
            "data": serializer.errors,
        }
    )


# home delete
@api_view(["DELETE"])
def home_delete(request, id):
    homeData = Home.objects.get(id=id)
    serializer = HomeSerializer(homeData)
    homeData.delete()
    return Response(
        {
            "message": "Data deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "data": serializer.data,
        }
    )
