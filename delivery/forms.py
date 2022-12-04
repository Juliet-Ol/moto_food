from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from delivery.models import User, Order, Profile, Post, Product

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2', 'is_admin', 'is_vendor', 'is_customer', 'is_rider')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'email', 'image', 'location', 'full_name', 'mobile_number')
        # fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  

        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'        








# from django import forms
# from delivery.models import User, Order, Profile 
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.db import transaction

# class CustomerSignUpForm(UserCreationForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=Order.objects.all().values_list(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_customer = True
#         user.save()
#         # customer = Customer.objects.create(user=user)
#         # customer.order.add(*self.cleaned_data.get('order'))
#         return user


# class VendorSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_vendor = True
#         if commit:
#             user.save()
#         return user

# class RiderSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_rider = True
#         if commit:
#             user.save()
#         return user		

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

# class ProfileForm(forms.Form):
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'password1', 'password2')

# class EditProfileForm(forms.Form):
#     class Meta:
#         # model = Profile
#         fields = '__all__'        

# class SignupForm(UserCreationForm):  
#     email = forms.EmailField(max_length=200, help_text='Required')  
#     class Meta:  
#         model = User  
#         fields = ('username', 'email', 'password1', 'password2')

# class PostForm(forms.Form):  
#     email = forms.EmailField(max_length=200, help_text='Required')  
#     class Meta:  
#         model = User  
#         fields = '__all__'     