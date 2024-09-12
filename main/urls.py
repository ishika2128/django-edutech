from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('products/', views.products, name='products'),
    path('cart/', views.view_cart, name='view_cart'),
    path('contact/', views.contact_us, name='contact_us'),
]
