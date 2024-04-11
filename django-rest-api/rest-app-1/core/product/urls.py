from django.urls import path

from .views import ProductView

urlpatterns = [
    path("", ProductView, name="product-list"),
    path("<id>/", ProductView, name="product-detail"),
]
