from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    # path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('vendor/', views.vendor, name='vendor'),
    path('rider/', views.rider, name='rider'),
    path('profile', views.profile, name='profile'), #check on the url slash
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post/', views.post, name='post'), #check on the url slash
    path('show_post', views.show_post, name='new_post'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    # path('checkout/', views.checkout, name='checkout'),
    path('approval/', views.approval, name='approval'),
    # path('update_item/', views.updateItem, name='update_item'),
    
    # path('view-post/<int:id>', views.viewPost, name="view-post"),
    # path('edit-post/<int:id>', views.editPost, name='edit-post'),

    # path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    
    # path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    # path('cart/item_increment/<int:id>/',
    #      views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/',
    #      views.item_decrement, name='item_decrement'),
    # path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    # path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)















# CartItem Urls
# urlpatterns += [
#     path('cart/', views.ListCart.as_view(), name='list-carts'),
    # path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
    # path('cart/create/', views.CreateCart.as_view(), name='create-cart'),
    # path('cart/<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
    # path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),

    # path('cartitem/', views.ListCartItem.as_view(), name='list-cartitem'),
    # path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
    # path('cartitem/create/', views.CreateItemCart.as_view(), name='create-cartitem'),
    # path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    # path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
# ]













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