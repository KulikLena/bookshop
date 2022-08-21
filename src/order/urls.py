
from django.contrib import admin
from django.urls import path, include
from order import views

app_name= 'order'
urlpatterns = [
    path('add_to_cart/', views.AddToCart.as_view(), name='add_to_cart'),
    path('delete_from_cart/<int:pk>/', views.DeleteFromCart.as_view(), name='delete_from_cart'),
    path('update_cart/', views.UpdateCart.as_view(), name='update_cart'),
    
]
