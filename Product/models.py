from tkinter import CASCADE
from urllib import request
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/products')
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    onboarded_at = models.DateField(auto_now=True)
    created_by = models.CharField(default='User', max_length=50)
    #created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class Requested_product(models.Model):
    requested_user = models.CharField(max_length=50)
    requested_item = models.CharField(max_length=50)
    requester_phone = models.IntegerField()
    requester_budget = models.CharField(max_length=50)
    requester_messsage = models.CharField(max_length=200)
    request_created_at = models.DateTimeField(auto_now_add=True)


