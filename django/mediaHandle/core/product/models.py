from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    # image = models.ImageField(upload_to="products", null=True, blank=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
