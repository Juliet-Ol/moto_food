import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm, PostForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def index(request):
    context ={}
    return render(request, 'moto/index.html', context)

def cart(request):
    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    context ={"cart":cart, "items":cartitems}
    return render (request, 'cart/cart.html', context) 

def store (request):

    products = Product.objects.all()
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    context = {'products': products, 'cart':cart}
    return render(request, 'cart/store.html', context)    


def update_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    action = data["action"]
      #added
    product = Product.objects.get(id=product_id)


    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, completed=False)
        
        cartitem = CartItem.objects.get(cart=cart, product=product)


        if action == 'inc':
            cartitem.quantity += 1
        else:
            cartitem.quantity -= 1

        if cartitem.quantity < 1:
            cartitem.delete()
        else:
            cartitem.save()

    return JsonResponse(cartitem.quantity, safe=False)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
      #added
    product = Product.objects.get(id=product_id)


    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)


        cartitem.quantity += 1

    #added to try add and remove    
        # if id == 'add': 
        #     cartitem.quantity += 1   
        
            
        

        # elif id == 'remove':
        #     cartitem.quantity -= 1 

        # if cartitem.quantity <= 0:
        #     cartitem.delete()       

        cartitem.save()

        num_of_items = cart.num_of_items
        print(cartitem)

    return JsonResponse(num_of_items, safe=False)






def checkout(request):
    
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.get(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    context = {'items': cartitems ,'cart':cart}
    return render(request,'cart/checkout.html', context)   



def post_checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, completed=False)
        cart.completed = True
        cart.save()
        messages.success(request, "Successfully made payments")

    return redirect ('index')   






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

def approval(request):
    user_list = User.objects.all()
    print(user_list)
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            
            #uncheck 
            user_list.update(approved=False)
            
            #update the database
            for x in id_list:
                user = User.objects.filter(id=int(x))
                print(user)
                user.update(approved=True)
                # User.objects.filter(pk=int(x)).update(approved=True) 

                rider = Rider.objects.filter(full_name=user.first().full_name)
                vendor = Vendor.objects.filter(full_name=user.first().full_name)

                if rider is not None: {
                    rider.update(approved=True)
                }

                if vendor is not None: {
                    vendor.update(approved=True)
                }
                # User.objects.filter(pk=int(x)).update(approved=False) 
                # Vendor.objects.filter(pk=int(x)).update(approved=False)
                # Rider.objects.filter(pk=int(x)).update(approved=False)
            print(id_list)

            messages.success(request, 'User successfully approved')  
            return redirect('index') 

        else:    
            return render (request,'registration/approval.html',{'user_list': user_list})
        
        
            # id_list = request.POST.getlist('boxes')
            # print(id_list)

    else:
        messages.success(request, 'you are not authorised to view this page')  

        return redirect('index')        



    # return render(request, 'registration/approval.html')


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
    form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        # print(request.POST['post'])
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Product()
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            author = current_user            
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            post = {'image':image, 'name':name, 'price':price, 'description': description  }
            form.save()
            messages.success(request, 'Saved product')
            print (post)

            return redirect ('/store')
        else:
            return render(request, 'food_vendor/new_post.html', {'form': form})

    else:
        return render(request, 'food_vendor/new_post.html', {'form': form})  


def show_post(request):  

    return render(request, 'food_vendor/show_post.html',)         


def new_post(request):  
    form = PostForm()
    return render(request, 'food_vendor/new_post.html', {'form' : form})   









# def store(request):
#     # if request.method == 'POST':
#     # if request.user.is_autheticated:
#     if request.user.customer:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         # order, created = Order.objects.get_or_create( complete=True)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []  
#         order ={'get_cart_total':0, 'get_cart_items':0,}
#         cartItems = order['get_cart_items']


#     products = Product.objects.all()
#     context = {'products': products, 'cartItems':cartItems }
#     return render(request, 'cart/store.html', context)     

# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)
#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     print(product)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)

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


# def cart(request):
#     # if request.method == 'POST':
#     # if request.user.is_autheticated:
#     if request.user.customer:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=True)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []  
#         order ={'get_cart_total':0, 'get_cart_items':0,}        
#         cartItems = order['get_cart_items']


#         # 'cartItems':cartItems

#     context = {'items': items ,'order':order, 'cartItems':cartItems}
#     return render(request,'cart/cart.html', context)        
    
# def checkout(request):
#     # if request.method == 'POST':
#     # if request.user.is_autheticated:
#     if request.user.customer:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []  
#         order ={'get_cart_total':0, 'get_cart_items':0,}
#         cartItems = order['get_cart_items']

#     context = {'items': items ,'order':order, 'cartItems':cartItems}
#     return render(request,'cart/checkout.html', context)   


# def checkout(request):
#     # if request.method == 'POST':
#     # if request.user.is_autheticated:
#     if request.user.customer:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []  
#         order ={'get_cart_total':0, 'get_cart_items':0,}

#     context = {'items': items ,'order':order}
#     return render(request,'cart/checkout.html', context)   








#





























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
























    

