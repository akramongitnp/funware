from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/products')
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
