from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def orders(request):
    return render(request, "dashboard/orders.html")


def products(request):
    return render(request, "dashboard/products.html")
