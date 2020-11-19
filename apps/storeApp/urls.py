from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('directions', views.directions),
    path('cart', views.cart),
    path('login', views.login),
    path('news', views.news),
    path('events', views.events),
    path('about_us', views.about_us),
    path('contact_us', views.contact_us),
    path('products/add_product', views.add_product),
    path('products/<int:product_id>', views.product_detail),
    path('create_product', views.create_product),
    path('create_category', views.create_category),
    path('create_brand', views.create_brand),
]