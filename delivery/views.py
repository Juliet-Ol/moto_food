import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm, PostForm
# from .models import Profile, Post
from .models import *
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
# from cart.cart import Cart


def index(request):
    return render(request, 'moto/index.html')

def store(request):
    # if request.method == 'POST':
    # if request.customer.is_autheticated:
    if request.user.is_customer:
        is_customer = request.user.is_customer
        # order, created = Order.objects.get_or_create(is_customer=is_customer, complete=False)
        # order, created = Order.objects.get_or_create( complete=True)
        # items = order.orderitem_set.all()
        # cartItems = order.get_cart_items
    else:
        items = []  
        order ={'get_cart_total':0, 'get_cart_items':0,}
        # cartItems = order['order.get_cart_items']


    products = Product.objects.all()
    context = {'products': products, }
    return render(request, 'cart/store.html', context)      




def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() 
            email = form.cleaned_data.get('email')    
            full_name = form.cleaned_data.get('full_name') 
            # restaurant_name = form.cleaned_data.get('restaurant_name')
            # description = form.cleaned_data.get('description')
            # location = form.cleaned_data.get('location')
            # approval = form.cleaned_data.get('approval')


            print (user, user.is_customer, email, full_name)
            print (user, user.is_vendor, email, full_name)
            print (user, user.is_rider, email, full_name)
            if user is not None and user.is_customer:
                customer = Customer.objects.create(user=user, email=email, full_name=full_name)

            elif user is not None and user.is_vendor:
                vendor = Vendor.objects.create(user=user, email=email, full_name=full_name)
                # restaurant_name=restaurant_name, description=description, location=location, approval=approval
                # login(request, user)
                # return redirect('vendor')
                
            elif user is not None and user.is_rider:
                rider = Rider.objects.create(user=user, email=email, full_name=full_name)
                # login(request, user)
                # return redirect('rider')      

            elif user is not None and user.is_admin:
                admin = Admin.objects.create(user=user, email=email, full_name=full_name)
                # login(request, user)
                # return redirect('adminpage')                 
                

                print(customer, vendor, rider)


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



# def approval(request):

#     user_list = User.objects.all()
#     print(user_list)
#     if request.user.is_superuser:
#         if request.method == "POST":
#             id_list = request.POST.getlist('boxes')
#             print(id_list)

            

#             messages.success(request, 'User successfully approved')  
#             return redirect('index') 

        

#         else:   
#             return render (request,'registration/approval.html',{'user_list': user_list})

#     else:
#         messages.success(request, 'you are not authorised to view this page')  

#         return redirect('index')  


#     return render (request,'registration/approval.html')    




# @login_required(login_url="/users/login")
# def cart_add(request, id):
#     user = request.user
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     order, created = Order.objects.get_or_create(id=id, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#     cart.add(product=product)
#     order.save()
#     orderItem.save()
#     print (cart)
#     print (product)
#     print (orderItem)
#     print(order)  
#     print(user)
    
       
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def item_clear(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.remove(product)
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def item_increment(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def item_decrement(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.decrement(product=product)
#     if product is None:
#         cart.remove(product)
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def cart_detail(request):
#     return render(request, 'cart/cart_detail.html')






# def logout_view(request):
#     return render(request, 'moto/index.html')  
# 
# 

def cart(request):
    if request.method == 'POST':
    # if request.user.is_autheticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        # cartItems = order.get_cart_items
    else:
        items = []  
        order ={'get_cart_total':0, 'get_cart_items':0,}        
        # cartItems = order['order.get_cart_items']


        # 'cartItems':cartItems

        context = {'items': items ,'order':order, }
    return render(request,'cart/cart.html', context)     

def checkout(request):
    if request.method == 'POST':
    # if request.user.is_autheticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []  
        order ={'get_cart_total':0, 'get_cart_items':0,}

        context = {'items': items ,'order':order}
    return render(request,'cart/checkout.html', context)     


def admin(request):
    return render(request,'profile/admin_profile.html')


def customer(request):
    return render(request,'profile/customer_profile.html')


def vendor(request):
    return render(request,'profile/vendor_profile.html')
    

def rider(request):
    return render(request,'profile/rider_profile.html')   


 


def edit_profile(request):

    # profile= Profile.objects.all()

    form = ProfileForm()

   
    return render(request, 'profile/edit_profile.html', {'form': form})      


def profile(request):
    form = ProfileForm(request.POST, request.FILES)
    # profile=Profile.objects.get(user= request.user.id)
    profile = Profile.objects.all()
    # profile=Profile.objects.get()
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
       
       
        if form.is_valid():
            print(profile)
            image=form.cleaned_data['image']  
            full_name=form.cleaned_data['full_name']  
            email=form.cleaned_data['email'] 
            # username=form.cleaned_data['username']
            profile = {'image':image, 'full_name':full_name, 'email':email}
            print(profile)
           
            # profile.username=request.user     

              
            form.save()            

            # profile=Profile.objects.get(author= request.user.id)
            # messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit_profile.html', {'form': form})

    # else:
        

    #     if Profile.objects.filter(user = request.user).count()
    #         profile = Profile(user=request.user, full_name=request.user.full_name, email=request.user.email)
    #         profile.save()
    else:
        # profile= request.user.profile 
        return render(request, 'profile/profile.html', {'form': form, 'profile':profile})      


def post(request):
    form = PostForm(request.POST, request.FILES)
    post = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        print(request.POST['post'])
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            # post = Post()
            post = form.save()
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            author = current_user            
            picture = form.cleaned_data['picture']
            price = form.cleaned_data['price']
            post = {'picture':picture, 'author':author, 'title':title, 'price':price }
            form.save()
            messages.success(request, 'Posted')
            print (post)

        # posts = Post.objects.all
        # context = {'posts': posts}

        return redirect ('store')
    else:
        return render(request, 'food_vendor/new_post.html', {'form': form})

        # else:
        # return render(request, 'food_vendor/new_post.html', {'form': form})  


def show_post(request):  

    return render(request, 'food_vendor/show_post.html',)      









# def post(request):
#     form = PostForm(request.POST, request.FILES)
#     post = Post.objects.all()
#     current_user = request.user
#     if request.method == 'POST':
#         print(request.POST['post'])
#         form = PostForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             # post = Post()
#             title = form.cleaned_data['title']
#             post = form.cleaned_data['post']
#             author = current_user            
#             picture = form.cleaned_data['picture']
#             price = form.cleaned_data['price']
#             post = {'picture':picture, 'author':author, 'title':title, 'price':price }
#             form.save()
#             messages.success(request, 'Posted')
#             print (post)

#             return redirect ('/show_post')
#         else:
#             return render(request, 'food_vendor/new_post.html', {'form': form})

#     else:
#         return render(request, 'food_vendor/new_post.html', {'form': form})  







# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)
#     is_customer = request.user.is_customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(is_customer=is_customer, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)

#     orderItem.save()

#     if orderItem.quantity <= 0:
#         orderItem.delete()

#     print(orderItem)

#     return JsonResponse('Item was added', safe=False)    



# get_total = sum (product.price*product.quantity)



# def editProfile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile= Profile.objects.filter(username=current_user)
#             print(profile)
#             if profile:
#                 print('profile exist')
#                 photo=form.cleaned_data['photo']  
#                 full_name=form.cleaned_data['full_name']  
#                 email=form.cleaned_data['email'] 
#                 username=form.cleaned_data['username']
#                 AuthenticationError=form.cleaned_data['AuthenticationError']
#                 Profile.objects.filter(username=current_user).update(email=email, full_name=full_name,photo=photo, username=username,AuthenticationError=AuthenticationError)
#             else:
#                 print('profile does not exist')
                
#                 print('profile does not exist')
#                 profile=form.save(commit=False)
#                 profile.username= current_user
#                 profile.save()

#             message='saved successfuly'
#             # profile_display(request)
#             return redirect(profile/profile.html)
    
            
#     else:
#         form = ProfileForm()
        
#     return render(request, 'profile/profile.html',{'form':form})      








# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)

#     if request.user.is_autheticated:
#         customer = request.user.customer
#         product = Product.objects.get(id=productId)
#         order, created = Order.objects.get_or_create(customer=request.customer, complete=False)
        
#         orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        
#         if action == 'add':
#             orderItem.quantity = (orderItem.quantity + 1)
#         elif action == 'remove': 
#             orderItem.quantity = (orderItem.quantity - 1)

#         orderItem.save()
        

#         if orderItem.quantity <= 0:
#             orderItem.delete()   
#     # if request.user.is_autheticated:
#     #     order, created = Order.objects.get_or_create(customer=request.customer, complete=False)
        
#         print(orderItem)
#     return JsonResponse('Item was added', safe=False)









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
























    

