from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from delivery.models import User, Order, Profile, Post, Product
# from  .models import CloudinaryField

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
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    # photo = forms.clo(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    mobile_number = forms.IntegerField(
        widget=forms.NumberInput(
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
        model = Profile
        fields = ('username', 'email', 'photo', 'location', 'full_name', 'mobile_number')

# class ProfileForm(forms.ModelForm):    
#     class Meta:
#         model = Profile
#         fields = ( 'email', 'photo', 'location', 'full_name', 'mobile_number')
#         fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  

        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'        
