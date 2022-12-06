import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from  cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


class Customer(models.Model):
    user =models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True)  

    def __str__(self):
        return self.full_name

class Product(models.Model):
    # user =models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,)
    # vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField( upload_to='profile_pics', default='')
   
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name  

class Order(models.Model): 
    # user =models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,)    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) 
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)
    #image
    def __str__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


        

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()        
        total = sum([item.get_total for item in orderitems])
        return total  

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()        
        total = sum([item.quantity for item in orderitems])
        return total     
 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    house_number = models.CharField(max_length=200, null=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address


class Approvals(models.Model):
    full_name = models.CharField(max_length = 100)
    verification = models.BooleanField(blank=False) 

class Admin(models.Model):
    user =models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, default='') 
    username = models.TextField()
    approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='approval')           

class Vendor(models.Model):  
    user =models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, default='')  
    full_name = models.CharField(max_length=100, blank=False)
    restaurant_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250) 
    # mobile_number = models.IntegerField(blank=False)
    email = models.EmailField(unique=True) 
    location = models.CharField(max_length=100)
    created_at = models.DateField(null=True, blank=True)
    photo =  CloudinaryField('image', default='')
    approved = models.BooleanField('Approved', default=False)

class Rider(models.Model): 
    user =models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, default='')  
    full_name = models.CharField(max_length=100)    
    description = models.TextField(max_length=250) 
    # mobile_number = models.IntegerField(blank=False)
    email = models.EmailField(unique=True) 
    location = models.CharField(max_length=100)
    created_at = models.DateField(null=True, blank=True)
    photo =  CloudinaryField('image', default='') 
    approved = models.BooleanField('Approved', default=False)                    



class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_vendor = models.BooleanField('Is vendor', default=False)
    is_rider = models.BooleanField('Is rider', default=False)
    # is_verified = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=False, default='', null=True)
    approved = models.BooleanField('Approved', default=False)
    # email = models.EmailField(max_length=100, blank=False)

    def save_user(self):
        self.save()

    def update_user(self):
        self.update()

    def delete_user(self):
        self.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)     
    mobile_number = models.IntegerField()
    location = models.CharField(max_length=100, default='')
    email = models.EmailField(null=True)      
    photo =  CloudinaryField('photo', default='https://res.cloudinary.com/dkcivjz16/image/upload/v1670318972/moto%20foods/rowan-freeman-clYlmCaQbzY-unsplash_saxitz.jpg') 
    

    def __str__(self):
        return f'{self.user.username} Profile'
        # return str(self.user.username)

class Post (models.Model):
    # vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)   
    published_date = models.DateTimeField(auto_now_add=True)
    picture = CloudinaryField('image')
    price = models.FloatField(default=False)
    # author = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True) 
    # food_rating = models.IntegerField(default=0)        


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    # created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)



    @property 
    def total_price(self):
        cartitems = self.cartitems.all()  
        total = sum([item.price for item in cartitems])    
        return total 

    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        return cartitems.count()
        # quantity = sum([item.quantity for item in cartitems])  
        # return quantity       


class CartItem(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    # date_added = models.DateField(auto_now_add=True)
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) 
    #image



    def __str__(self):
        return self.product.name   


    @property
    def price(self):  
        new_price = self.product.price * self.quantity 
        return new_price