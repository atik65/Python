from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Product

# Create your views here.

# products_view


def products_view(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")

        if name:
            # create product
            product = Product.objects.create(name=name)
            product.save()
            messages.error(request, "Product created successfully")
            return redirect("products_view")

        else:
            messages.error(request, "Name is required")
            return redirect("products_view")

    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


# product_details_view
def product_details_view(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, "products/product_details.html", {"product": product})


# delete product
def delete_product(request, id):
    product = Product.objects.filter(id=id).first()
    product.delete()
    messages.error(request, "Product deleted successfully")
    return redirect("products_view")


# update product
def update_product(request, id):
    # product = Product.objects.filter(id=id).first()
    # if request.method == "POST":
    #     data = request.POST
    #     name = data.get("name")

    #     if name:
    #         product.name = name
    #         product.save()
    #         messages.error(request, "Product updated successfully")
    #         return redirect("products_view")

    #     else:
    #         messages.error(request, "Name is required")
    #         return redirect("products_view")
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        data = request.POST
        name = data.get("name")

        if name:
            product.name = name
            product.save()
            messages.success(request, "Product updated successfully")
            return redirect("products_view")
        else:
            messages.error(request, "Name is required")
            return redirect("products_view")

    return render(request, "products/update_product.html", {"product": product})
