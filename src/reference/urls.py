from django.contrib import admin
from django.urls import path
#from . import views 
from reference import views

urlpatterns = [
    path('auth/add/<int:pk>/', views.AuthorDetail.as_view(),name="auth-det" ),
    path('auth/add/', views.AuthorAdd.as_view(), name="auth-add"),
    path('auth/list/', views.AuthorList.as_view(), name="auth-list"),
    path('pub/add/<int:pk>/', views.PublisherDetail.as_view(), name="pub-det"),
    path('pub/add/', views.PublisherAdd.as_view(), name="pub-add"),
    path('pub/list/', views.PublisherList.as_view(), name="pub-list"),
]
