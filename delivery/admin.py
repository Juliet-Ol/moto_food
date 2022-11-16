from django.contrib import admin
from .models import User
from .models import Profile, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Order)














# from django.contrib import admin
# from.models import Vendor, Customer, Order, Profile, User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User

# from django.contrib.auth.admin import UserAdmin
# from .models import User

# class SignupForm(UserCreationForm):
#     class Meta:         
#         model = User  
#         fields = ('username', 'email', 'password1', 'password2')

# class MyUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', )

# class MyUserAdmin(UserAdmin):
#     form = MyUserChangeForm
#     add_form = SignupForm        
        

# admin.site.register(User, MyUserAdmin)
# admin.site.register(Vendor)
# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(Profile)
