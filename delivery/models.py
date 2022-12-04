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

    # def __str__(self):
    #     return self.name   

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url

    #     except:  
    #         url = ''
    #     return url       



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

    # @property
    # def get_sum_total(self):
    #     price = self.product.deal_price
    #     quantity = self.quantity
    #     total = sum(price*quantity)
    #     # total = sum(product.get_sum_total for product in productItem)
    #     return total       

    
 

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
  
    

#     def __str__(self):
#         return self.full_name

# class Tag(models.Model):
#     full_name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.full_name   

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
    mobile_number = models.IntegerField(default='')
    location = models.CharField(max_length=100, default='')
    email = models.EmailField(null=True)  
    
    photo =  CloudinaryField('photo', default='') 
    image = models.ImageField( upload_to='profile_pics', default='default.jpg', ) 
       
    # photo = models.ImageField(default='default.jpg', upload_to='profile_pics' ) 
    # photo =  CloudinaryField('photo', default='')   

    def __str__(self):
        return f'{self.user.username} Profile'

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

     


    
    # @property
    # def get_total(self):
    #     total = self.product.price * self.quantity
    #     return total           











# class Order(models.Model):  
#     status = models.CharField(max_length=100)
#     vendor_name = models.CharField(max_length=100, blank=False) 
#     created_at = models.DateTimeField(auto_now=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')       




# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price_ht = models.FloatField(blank=True)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

#     # TAX_AMOUNT = 19.25

#     def price_ttc(self):
#         return self.price_ht 

#     def __str__(self):
#         return  self.client + " - " + self.product







# from django.db import models
# from django.utils import timezone
# from  cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User
# from django.conf import settings




# from django.contrib.auth.models import AbstractUser      
# # from django.contrib.auth import get_user_model
# # User = get_user_model()


# class User(AbstractUser):
#       ADMIN = 1
#       VENDOR = 2
#       CUSTOMER = 3
#       RIDER = 4
      
#       ROLE_CHOICES = (
#           (ADMIN, 'admin'),
#           (VENDOR, 'vendor'),
#           (CUSTOMER, 'customer'),
#           (RIDER, 'rider'),
          
#       )
#       role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)






# # class User(AbstractUser):
# #     is_admin = models.BooleanField('admin status', default=False)
# #     is_customer = models.BooleanField('customer status', default=False)
# #     is_vendor = models.BooleanField('vendor status', default=False)
# #     is_rider = models.BooleanField('rider status', default=False)  
# #     # is_verified = models.BooleanField(default=False)
# #     # full_name = models.CharField(max_length=100, blank=False)
# #     # email = models.EmailField(max_length=100, blank=False)

# #     def save_user(self):
# #         self.save()

# #     def update_user(self):
# #         self.update()

# #     def delete_user(self):
# #         self.delete()


# class Profile(models.Model):
#     full_name = models.CharField(max_length=100, blank=False)
     
#     mobile_number = models.IntegerField(default='')
#     location = models.CharField(max_length=100, default='')
#     email = models.EmailField(null=True) 
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default='')    
#     photo =  CloudinaryField('image', default='')  



# class Order(models.Model):  
#     status = models.CharField(max_length=100)
#     vendor_name = models.CharField(max_length=100, blank=False) 
#     created_at = models.DateTimeField(auto_now=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

# class Requests(models.Model):  
    
#     verification = models.BooleanField()  

 


# class Vendor(models.Model):   
#     full_name = models.CharField(max_length=100, blank=False)
#     restaurant_name = models.CharField(max_length=100, blank=False)
#     description = models.TextField(null=True) 
#     mobile_number = models.IntegerField(blank=False)
#     email = models.EmailField(unique=True) 
#     location = models.CharField(max_length=100, blank=False)
#     created_at = models.DateTimeField(null=True, blank=True, default='')
#     photo =  CloudinaryField('image', default='')
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.full_name

# class Tag(models.Model):
#     full_name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.full_name    


# class Customer(models.Model):    
#     full_name = models.CharField(max_length=100, blank=False)
#     email = models.EmailField(unique=True) 
#     mobile_number = models.IntegerField(blank=False)
#     location = models.CharField(max_length=100, blank=False)
#     created_at = models.DateTimeField(auto_now=True)
#     photo =  CloudinaryField('image', default='')
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

# class Rider(models.Model): 
#     full_name = models.CharField(max_length=100, blank=False)
#     email = models.EmailField(unique=True) 
#     mobile_number = models.IntegerField(blank=False)
#     location = models.CharField(max_length=100, blank=False)
#     created_at = models.DateTimeField(auto_now=True)
#     photo =  CloudinaryField('image', default='') 
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# class Admin(models.Model):
#     username = models.TextField()
#     requests = models.ForeignKey(Requests, on_delete=models.CASCADE, related_name='requests')    











# # from django.db import models
# # from cloudinary.models import CloudinaryField
# # from django.conf import settings

# # from django.contrib.auth.models import User
# # # import datetime
# # from django.utils import timezone
# # # from django.utils.dateparse import (
# # #     parse_date, parse_datetime, parse_duration, parse_time,

# # # )


# # from django.contrib.auth.models import AbstractUser      

# # class User(AbstractUser):
# #     is_admin = models.BooleanField('admin status', default=False)
# #     is_customer = models.BooleanField('customer status', default=False)
# #     is_vendor = models.BooleanField('vendor status', default=False)
# #     is_rider = models.BooleanField('rider status', default=False)  
# #     # is_verified = models.BooleanField(default=False)
# #     # full_name = models.CharField(max_length=100, blank=False)
# #     # email = models.EmailField(max_length=100, blank=False)

# #     def save_user(self):
# #         self.save()

# #     def update_user(self):
# #         self.update()

# #     def delete_user(self):
# #         self.delete() 




# # # class Approvals(models.Model):
# # #     full_name = models.CharField(max_length = 100)
# # #     verification = models.BooleanField(blank=True)

# # class Admin(models.Model):
# #     username = models.TextField()
# #     # approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='approval')


# # class Vendor(models.Model):   
# #     full_name = models.CharField(max_length=100, blank=False)
# #     restaurant_name = models.CharField(max_length=100, blank=False)
# #     description = models.TextField(null=True) 
# #     mobile_number = models.IntegerField(blank=False)
# #     email = models.EmailField(unique=True) 
# #     location = models.CharField(max_length=100, blank=False)
# #     created_at = models.DateField(null=True, blank=True)
# #     photo =  CloudinaryField('image', default='')
# #     # approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='vendor_approval')
# #     # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# #     def __str__(self):
# #         return self.full_name

# # class Tag(models.Model):
# #     full_name = models.CharField(max_length=100, null=True)

# #     def __str__(self):
# #         return self.full_name   

# # class Rider(models.Model):   
# #     full_name = models.CharField(max_length=100, blank=False)
# #     restaurant_name = models.CharField(max_length=100, blank=False)
# #     description = models.TextField(null=True) 
# #     mobile_number = models.IntegerField(blank=False)
# #     email = models.EmailField(unique=True) 
# #     location = models.CharField(max_length=100, blank=False)
# #     created_at = models.DateField(null=True, blank=True)
# #     photo =  CloudinaryField('image', default='') 
# #     # approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='customer_approval', default='')


# # class Customer(models.Model):    
# #     full_name = models.CharField(max_length=100)
# #     email = models.EmailField(unique=True) 
# #     mobile_number = models.IntegerField(blank=False)
# #     location = models.CharField(max_length=100, blank=False)
# #     created_at = models.DateField(null=True, blank=True)
# #     photo =  CloudinaryField('image', default='')
# #     # approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='customer_approval', default='')
# #     # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# #     def __str__(self):
# #         return self.full_name




# # class Order(models.Model):    
# #     # user = models.IntegerField(blank=False)
# #     status = models.CharField(max_length=100)
# #     vendor_name = models.CharField(max_length=100, blank=False) 
# #     created_at = models.DateField(null=True, blank=True)
# #     price = models.DecimalField(max_digits=6, decimal_places=2)
# #     # approval = models.ForeignKey(Approvals, on_delete=models.CASCADE, related_name='customer_approval', default='')
# #     # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

# # class Profile(models.Model):
# #     full_name = models.CharField(max_length=100, default='')     
# #     mobile_number = models.IntegerField(default='')
# #     location = models.CharField(max_length=100, default='')
# #     email = models.EmailField(null=True) 
# #     # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')    
# #     photo =  CloudinaryField('image', default='')
    




    



