from contextlib import redirect_stderr
from multiprocessing import context
from typing import ItemsView
from urllib import request
from django.shortcuts import render
from .models import Requested_product, Product


def requested_product(request):
    user = request.POST['name']
    item = request.POST['items']
    phone = request.POST['phone']
    budgets = request.POST['budgets']
    message = request.POST['message']
    data = Requested_product(requested_user = user, requested_item = item, requester_phone = phone, requester_budget = budgets, requester_messsage = message)
    data.save()
    items = Requested_product.objects.all()
    context = {'item': items}
    return render(request, 'try.html', context)

def feedpost(request):
    name = request.POST['product_name']
    price = request.POST['product_price']
    desc = request.POST['product_desc']
    img = request.POST['product_img']
    type = request.POST['product_type']
    model = request.POST['product_model']
    created_by = request.user.first_name + ' ' + request.user.last_name
    data = Product(name = name, price = price, description = desc, image = img, type = type, model = model, created_by = created_by)
    data.save()
    items = Product.objects.all()
    context = {'item' : items}
    return render(request, 'try.html', context)
