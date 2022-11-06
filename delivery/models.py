from django.db import models
from cloudinary.models import CloudinaryField

class Vendor(models.Model):
    # id = models.IntegerField(blank=False)
    full_name = models.CharField(max_length=100, blank=False)
    restaurant_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True) 
    mobile_number = models.IntegerField(blank=False)
    email = models.EmailField(unique=True) 
    location = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo =  CloudinaryField('image', default='')
    approval = models.BooleanField (max_length=100, blank=False)

class Customer(models.Model):
    # id = models.IntegerField(blank=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    mobile_number = models.IntegerField(blank=False)
    location = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo =  CloudinaryField('image', default='')

class Order(models.Model):
    # id = models.IntegerField(blank=bool)
    user_id = models.IntegerField(blank=bool)
    status = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100, blank=False) 
    created_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Profile(models.Model):
    avatar = models.ImageField(upload_to='image', null=True)   
    name =models.CharField(max_length=50, blank=True)
    bio = models.TextField(null=True)



