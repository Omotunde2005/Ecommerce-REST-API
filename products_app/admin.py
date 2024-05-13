from django.contrib import admin
from products_app import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.Sale)
admin.site.register(models.SaleItem)