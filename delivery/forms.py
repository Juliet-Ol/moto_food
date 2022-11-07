from django import forms
from . models import Vendor, Customer, Order, Profile 
from django.contrib.auth.models import UserCreationForm



class VendorForm(forms.form):
    class Meta:
        model = Vendor
        fields = '__all__'


class CustomerForm(forms.form):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.form):
    class Meta:
        model = Order
        fields = '__all__'

class ProfileForm(forms.form):
    class Meta:
        model = Profile
        fields = '__all__'

