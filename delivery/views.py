from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from .models import Vendor, Customer, Order, Profile
from django.contrib import messages
from .forms import VendorForm, CustomerForm, OrderForm, ProfileForm

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request, 'moto/index.html') 


def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
   
            profile = Customer()
            profile.full_name = form.cleaned_data['username']
            # profile.delivery = None
            # profile.user = user
            profile.save()

            messages.success(request, 'User has been registered')

            subject = 'welcome to Moto food'
            message = f'Hi {user.username}, thank you for registering for Moto food'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )

            return redirect ('/accounts/login')
        else:
            return render(request, 'registration/signup.html', {'form': form})

    else:
        return render(request, 'registration/signup.html', {'form': form})    


    

