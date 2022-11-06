from django.db import models
from cloudinary.models import CloudinaryField



class Approvals(models.Model):
    full_name = models.CharField(max_length = 100)
    verification = models.BooleanField



class Vendor(models.Model):   
    full_name = models.CharField(max_length=100, blank=False)
    restaurant_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True) 
    mobile_number = models.IntegerField(blank=False)
    email = models.EmailField(unique=True) 
    location = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo =  CloudinaryField('image', default='')
    approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='vendor_approval')

class Customer(models.Model):    
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    mobile_number = models.IntegerField(blank=False)
    location = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo =  CloudinaryField('image', default='')
    approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='customer_approval')

class Order(models.Model):    
    user_id = models.IntegerField(blank=bool)
    status = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100, blank=False) 
    created_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Profile(models.Model):
    avatar = models.ImageField(upload_to='image', null=True)   
    name =models.CharField(max_length=100, blank=True)
    bio = models.TextField(null=True)


class Admin(models.Model):
    username = models.TextField()
    approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='approval')
    
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin=models.BooleanField('Is admin', default=False)
    is_vendor= models.BooleanField('Is Vendor', default=False)
    is_customer=models.BooleanField('Is Customer', default=False)


