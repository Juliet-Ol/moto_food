from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from .models import Vendor, Customer, Order, Profile
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request, 'moto/index.html', {'name': 'Juliet'}) 




    

