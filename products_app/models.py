from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=20, unique=False, blank=False, null=False)
    email = models.CharField(max_length=30, unique=True, blank=False, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Product(models.Model):
    store = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=20, unique=False, blank=False, null=False, name="Title")
    description = models.TextField(max_length=200, unique=False, blank=False, null=False, name="Description")
    price = models.IntegerField(unique=False, blank=False, null=False, name="Price")
    image = models.ImageField(upload_to="product_images", name="Image")
    url = models.CharField(max_length=7, name="URL", null=True, blank=True)


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, blank=True, through="SaleItem")
    date = models.DateTimeField(auto_now=True, null=True)


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1, null=True)
    date = models.DateTimeField(auto_now=True, null=True)