"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from forecast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forecast/', views.show_forecast_view),
    path ('main_page/', views.show_mainpage_view),
    path ('book_page/', views.BookPage.as_view()),
    path('book/<int:id>/', views.BookDetailView.as_view()),
    path ('map_page/', views.MapPage.as_view()),
    #path ('book_add/', views.book_add_view),
    
    path ('book_add/', views.BookAdd.as_view()),
    
]
