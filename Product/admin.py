from django.contrib import admin
from Product.models import Product, Requested_product

admin.site.register(Product),
admin.site.register(Requested_product)

