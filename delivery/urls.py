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
    # path('show_post', views.show_post, name='show_post'),
    # path('new_post', views.post, name='new_post'),
    path('store', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('update_cart', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('post_checkout/', views.post_checkout, name='post_checkout'),
    # path('checkout/<str:pk>', views.checkout, name='checkout'),
    path('approval/', views.approval, name='approval'),    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
























