"""
URL configuration for Resturant_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView),
    path('book_table/',BookTableView,name="book_table"),
    path('menu/',MenuView,name="menu"),
    path('about/',AboutView,name="about"),
    path('feedback/',Feedbacks,name="feedback"),
    path('cart/', cart_view, name='cart_view'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:food_id>/',remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('checkout/', checkout_view, name='checkout'),
    path('place-order/', place_order, name='place_order'),
    path('order-success/',order_success, name='order_success'),
    path('orders/',my_orders_view, name='orders'),
    path('login/',Login_page,name='login'),
    path('signup/',Signup,name='signup'),
    path('logout',Logout_page,name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    