from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm, EditProfileForm
from .models import Profile



def index(request):
    return render(request, 'moto/index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'registration/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_vendor:
                login(request, user)
                return redirect('vendor')
            elif user is not None and user.is_rider:
                login(request, user)
                return redirect('rider')    
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


# def logout_view(request):
#     return render(request, 'moto/index.html')    


def admin(request):
    return render(request,'profile/admin_profile.html')


def customer(request):
    return render(request,'profile/customer_profile.html')


def vendor(request):
    return render(request,'profile/vendor_profile.html')
    

def rider(request):
    return render(request,'profile/rider_profile.html')   


def cart(request):
    context = {}
    return render(request, 'cart/cart.html')     


def editProfile(request):
    form = EditProfileForm(initial={'name':request.user.username, 'location':'test'})

   
    return render(request, 'profile/edit_profile.html', {'form': form})      


def profile(request):
    form = ProfileForm(request.POST, request.FILES)
    # profile=Profile.objects.get(user= request.user.id)
    profile = Profile.objects.all().update()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
       
       
        if form.is_valid():
            # profile.photo=form.cleaned_data['photo']  if len(request.FILES) != 0 else profile.photo 
            # profile.full_name=form.cleaned_data[' full name']  
            # profile.email=form.cleaned_data['email'] 
            profile.user=request.user      

              
            
            profile.save()

            

            # profile=Profile.objects.get(author= request.user.id)
            # messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    # else:
        

    #     if Profile.objects.filter(user = request.user.id).count() == 0:
    #         profile = Profile(user=request.user, full_name=request.user.full_name, email=request.user.email)
    #         profile.save()
    else:
        # profile= request.user.profile 
        return render(request, 'profile/profile.html', {'form': form, 'profile':profile})      




















# from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpRequest
# from .models import Vendor, Customer, Order, Profile
# from django.contrib import messages
# from .forms import CustomerSignUpForm, VendorSignUpForm, RiderSignUpForm, ProfileForm, EditProfileForm, PostForm
# from django.contrib.auth.models import User
# from django.views.generic import CreateView

# from django.conf import settings
# from django.core.mail import send_mail




# def index(request):
#     return render(request, 'moto/index.html')


# def register_landing(request):
#     context = {}
#     return render(request, 'moto/register_landing.html')     

# def cart(request):
#     context = {}
#     return render(request, 'cart/cart.html') 

# def checkout(request):
#     context = {}
#     return render(request, 'cart/checkout.html') 

# def post(request):    
#     form = PostForm
#     current_user = request.user
#     if request.method == 'POST':
#         # print(request.POST['post'])
#         form = PostForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             # post = Post()
#             # title = form.cleaned_data['title']
#             # post = form.cleaned_data['post']
#             # author = current_user
#             # post.projecturl= form.cleaned_data['projecturl']
#             # post.photo = form.cleaned_data['photo']
#             post.save()
#             messages.success(request, 'Posted')

#             return redirect ('index')
#         else:
#             return render(request, 'food_vendor/post.html', {'form': form})

#     else:
#         return render(request, 'food_vendor/post.html')  
   
      





# # def register(request):
# #     form = UserCreationForm

# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
   
# #             profile = Profile()
# #             profile.full_name = form.cleaned_data['full name']
# #             profile.email=form.cleaned_data['email'] 
# #             profile.photo = form.cleaned_data['photo']
# #             profile.user = user
# #             profile.save()
            
# #             return redirect ('/profile')
# #         else:
# #             return render(request, 'registration/signup.html', {'form': form})

# #     else:
# #         return render(request, 'registration/signup.html', {'form': form})   



# def editProfile(request):
#     form = EditProfileForm(initial={'name':request.user.username, 'location':'test'})

   
#     return render(request, 'profile/edit_profile.html', {'form': form})      


# def profile(request):
#     form = ProfileForm(request.POST, request.FILES)
#     # profile=Profile.objects.get(user= request.user.id)
#     profile = Profile.objects.all().update()
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
       
       
#         if form.is_valid():
#             # profile.photo=form.cleaned_data['photo']  if len(request.FILES) != 0 else profile.photo 
#             # profile.full_name=form.cleaned_data[' full name']  
#             # profile.email=form.cleaned_data['email'] 
#             profile.user=request.user      

              
            
#             profile.save()

            

#             # profile=Profile.objects.get(author= request.user.id)
#             # messages.success(request, 'Profile has been updated')

#             return redirect ('/profile')
#         else:
#             return render(request, 'profile/edit.html', {'form': form})

#     # else:
        

#     #     if Profile.objects.filter(user = request.user.id).count() == 0:
#     #         profile = Profile(user=request.user, full_name=request.user.full_name, email=request.user.email)
#     #         profile.save()
#     else:
#         # profile= request.user.profile 
#         return render(request, 'profile/profile.html', {'form': form, 'profile':profile}) 




# class SignUpView(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'registration/signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'admin'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         # return redirect('customer:food_list')
#         return redirect('registration/signup.html')



# class CustomerSignUpView(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name = 'registration/signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'customer'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('customers')

# class VendorSignUpView(CreateView):
#     model = User
#     form_class = VendorSignUpForm
#     template_name = 'registration/signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'vendorr'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('registration/signup.html')

# class RiderSignUpView(CreateView):
#     model = User
#     form_class = RiderSignUpForm
#     template_name = 'registration/signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'rider'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('registration/signup.html')   
























    

