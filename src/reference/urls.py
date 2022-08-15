from django.contrib import admin
from django.urls import path
#from . import views 
from reference import views

urlpatterns = [
    path('auth/add/<int:pk>/', views.AuthorDetail.as_view() ),
    path('auth/add/', views.AuthorAdd.as_view()),
    path('auth/list/<int:pk>/', views.AuthorDetail.as_view()),
    path('auth/list/', views.AuthorList.as_view()),
    path('pub/add/<int:pk>/', views.PublisherDetail.as_view()),
    path('pub/add/', views.PublisherAdd.as_view()),
    path('pub/list/', views.PublisherList.as_view()),
]
