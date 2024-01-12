from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('blog',views.blog),
    path('contact',views.contact),
    path('gallery',views.gallery),
    path('service',views.service),
    path('typography',views.typography),
    path('register',views.register),
    path('login',views.login),
    path('GYMREGISTER',views.GYMREGISTER),
    
]
