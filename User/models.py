from email.mime import image
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='http://bootdey.com/img/Content/avatar/avatar1.png', upload_to='assets/profile')
    phone = models.IntegerField(default=None, blank=True, null=True)
    store = models.CharField(max_length=50, default=None, blank=True, null=True)
    location = models.CharField(max_length=50, blank= True, null=True, default=None)
    DOB = models.DateField(default=None, blank=True, null=True)
    def __str__(self):
        return f'{self.user.username} Profile'
