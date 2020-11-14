from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news', views.news),
    path('events', views.events),
    path('about_us', views.about_us),
    path('contact_us', views.contact_us),
]