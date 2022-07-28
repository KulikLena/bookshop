from django.contrib import admin
from django.urls import path
#from . import views 
from reference import views

urlpatterns = [
    path('auth/<int:id>/', views.AuthorDetail.as_view(),name="auth-det" ),
    path('auth/add/', views.AuthorAdd.as_view(), name="auth-add"),
    path('pub/<int:id>/', views.PublisherDetail.as_view(), name="pub-det"),
    path('pub/add/', views.PublisherAdd.as_view(), name="pub-add"),
]
