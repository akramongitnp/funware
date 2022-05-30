from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='assets/profile')
    def __str__(self):
        return f'{self.user.username} Profile'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/products')
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
