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
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)


        cartitem.quantity += 1      

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


           
            if user is not None and user.is_customer:
                customer = Customer.objects.create(user=user, email=user.email, full_name=user.full_name)
                # profile = Profile.objects.create(user=user, email=user.email, full_name=user.full_name, )

            elif user is not None and user.is_vendor:
                vendor = Vendor.objects.create(user=user, email=user.email, full_name=user.full_name)
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
    # profile=Profile.objects.get(user= request.user)
    profile = Profile.objects.all()
    # profile=Profile.objects.get()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
       
       
        if form.is_valid():
            print(profile)
           
            photo=form.cleaned_data['photo']  
            full_name=form.cleaned_data['full_name']  
            email=form.cleaned_data['email'] 
            # username=form.cleaned_data['username']
            profile = { 'photo':photo, 'full_name':full_name, 'email':email}
            print(profile, photo)
           
            # profile.username=request.user     

              
            form.save() 

                     

            # profile=Profile.objects.get(author= request.user.id)
            # messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit_profile.html', {'form': form})

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