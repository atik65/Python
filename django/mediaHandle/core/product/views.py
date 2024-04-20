from django.shortcuts import HttpResponse, render


# Create your views here.
def products(request):
    return HttpResponse("Products will be here!")
