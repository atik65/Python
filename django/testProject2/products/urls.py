from django.urls import path

from . import views

urlpatterns = [
    path("", views.products_view, name="products_view"),
    path("<id>/", views.product_details_view, name="product_details_view"),
    path("<id>/delete/", views.delete_product, name="delete_product"),
    path("update/<id>/", views.update_product, name="update_product"),
]
