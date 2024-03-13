from django.http import HttpResponse
from django.shortcuts import render


# home view
def home(request):
    context = {"name": "John", "age": 30, "scores": [10, 20, 30, 40, 50]}
    return render(request, "home.html", context)


# about view
def about(request):
    return render(request, "about.html")


# service view
def service(request):
    return render(request, "service.html")
