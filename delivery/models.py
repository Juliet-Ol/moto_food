from django.db import models
from django.contrib.auth.models import AbstractUser
from  cloudinary.models import CloudinaryField
from django.contrib.auth.models import User




class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_vendor = models.BooleanField('Is vendor', default=False)
    is_rider = models.BooleanField('Is rider', default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)     
    mobile_number = models.IntegerField(default='')
    location = models.CharField(max_length=100, default='')
    email = models.EmailField(null=True)       
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics' ) 
    photo =  CloudinaryField('photo', default='')   

    def __str__(self):
        return f'{self.user.username} Profile'

class Post (models.Model):
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)   
    published_date = models.DateTimeField(auto_now_add=True)
    picture = CloudinaryField('image')
    food_rating = models.IntegerField(default=0)        


class Order(models.Model):  
    status = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100, blank=False) 
    created_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')       










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
    




    



