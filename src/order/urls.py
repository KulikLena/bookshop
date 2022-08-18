
from django.contrib import admin
from django.urls import path, include
from order import views

app_name= 'order'
urlpatterns = [
    path('add_to_cart/', views.AddToCart.as_view(), name='add_to_cart'),
]
