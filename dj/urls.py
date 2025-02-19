"""
URL configuration for dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yolo.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/<adad>', catg),
    path('', home),
    path('404/', error),
    path('about/', about),
    path('address/' , address),
    path('blog/', blog),
    path('blogd/<adad>', blogd),
    path('cart/', cart),
    path('comingsoon/', comingsoon),
    path('contact/', contact),
    path('faqs/', faqs),
    
    path('login/', login),
    path('logout/', logout),
    path('onsale/', onsale),
    path('ordersuccess/', ordersuccess),
    
    path('product/<adad>', product),
    path('register/', register),
    
    path('search/', search),
    path('shop/', shop),
    path('success/', success),
    path('user/', user),
    path('uservip/', uservip),
    path('wishlist/', wishlist),
    path('addcart/<pid>', addcart),
    path('addwish/<pid>', addwish),
    path('deletecart/<itmid>', deletecart),
    path('deletewish/<itmid>', deletewish),
    path('pluscart/<itmid>', pluscart),
    path('minuscart/<itmid>', minuscart),
    path('addaddress/<aid>', addaddress),
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
