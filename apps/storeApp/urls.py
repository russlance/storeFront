from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news', views.news),
    path('events', views.events),
    path('about_us', views.about_us),
    path('contact_us', views.contact_us),
    path('add_product', views.add_product),
    path('create_product', views.create_product),
]