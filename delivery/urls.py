from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin

from . import views
from delivery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)