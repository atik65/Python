from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("orders", views.orders, name="orders"),
    path("products", views.products, name="products"),
]
