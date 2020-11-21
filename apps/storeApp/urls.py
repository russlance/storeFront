from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('navbar', views.navbar),
    path('directions', views.directions),
    path('cart', views.cart),
    path('login', views.login),
    path('news', views.news),
    path('events', views.events),
    path('about_us', views.about_us),
    path('contact_us', views.contact_us),
    # path('products/add_product', views.add_product),
    path('products/<int:product_id>', views.product_detail),
    path('products/<int:product_id>/assign_to_sale', views.assign_to_sale),
    path('products/add_to_cart', views.add_to_cart),
    path('create_sale', views.create_sale),
    path('create_product', views.create_product),
    path('create_category', views.create_category),
    path('create_brand', views.create_brand),
    path('users/register', views.register_user),
    path('users/login', views.log_in),
    path('users/logout', views.log_out),
    path('admin/home', views.admin_home),
]