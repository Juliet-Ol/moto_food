from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    # path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('vendor/', views.vendor, name='vendor'),
    path('rider/', views.rider, name='rider'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile', views.editProfile, name='edit_profile'),
    path('cart', views.cart, name='cart'),
    
]

















# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# # from django.contrib import admin

# from . import views
# from delivery import views
# from delivery.views import Customer, Vendor

# urlpatterns = [
#     path('', views.index, name='index'),
#     # path('register/', views.register, name='register'),
#     path('accounts/register/', views.SignUpView.as_view(), name='register'),
#     path('accounts/signup/customer/', views.CustomerSignUpView.as_view, name='customer_signup'),
#     path('accounts/signup/vendor/', views.VendorSignUpView.as_view, name='vendor_signup'),
#     path('accounts/signup/rider/', views.RiderSignUpView.as_view, name='rider_signup'),
   
#     path('profile/', views.profile, name='profile'),
#     path('edit_profile', views.editProfile, name='edit_profile'),
#     path('cart', views.cart, name='cart'),
#     path('checkout', views.checkout, name='checkout'),
#     path('post', views.post, name='post'),
#     path('register_landing/', views.register_landing, name='register-landing'),
    
# ]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)